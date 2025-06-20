#include "IGoal.h"
#include "../../../Public/Utils/Time.h"
#include "Public.h"
#include "Utils/Utils.h"
#include "../AICondition/AIConFactory.h"

IGoal::IGoal(int32_t nCfgId)
{
    m_CfgId = nCfgId;
    Init(nCfgId);
}

void IGoal::Init(int32_t nCfgId)
{
    //init data from cfg Table_Goal
	Table_NpcAIGoalSensor * pGoalCfg = TABLE_GET_BY_ID(Table_NpcAIGoalSensor)(nCfgId);
	if (nullptr == pGoalCfg)
	{
		LOG_ERROR("IGoal::Init, GoalCfg is null, CfgId:{}", nCfgId);
		return;
	}
	m_Id = gGenGoalId.generate(); // Generate a unique ID for the goal
	m_EGaolType = static_cast<E_AIGoalType>(pGoalCfg->GetType());
	m_Weight = pGoalCfg->GetPrority();
	m_LastCalGoalTime = TimeHelper::getCurrentTimestamp();
	//初始化条件
	std::string conditionList = pGoalCfg->GetConditionList();
	if (!conditionList.empty())
	{
		std::vector<int32_t> conditions = solar::StringUtils::SplitString(conditionList);
		for (const auto& con : conditions)
		{
			Table_NpcAICondition* pCondition = TABLE_GET_BY_ID(Table_NpcAICondition)(con);
			if (pCondition)
			{
				IAICon* pAICon = AIConFactory::CreateAICondition(pCondition);
                if (pAICon)
                {
					AddCondition(pAICon);
                }
                else
                {
					LOG_ERROR("IGoal::Init, CreateAICondition failed, CfgId:{}, ConditionId:{}", m_CfgId, con); 
                }
			}
            else
            {
				LOG_ERROR("IGoal::Init, ConditionCfg is null, CfgId:{}, ConditionId:{}", m_CfgId, con); 
            }
		}
	}
}

void IGoal::OnUpdate(const AIKnowledge* pknowledge)
{
    do{
        //已满足且未过期，则不更新
        if(IsGoalSatisfy() && !IsTimeOut())
            break;
        //Goal,超时了，则重新计算
        if(IsGoalSatisfy() && IsTimeOut())
        {
           Reset(); 
        }

        //是否在CD中
        if(InCalGoalCD())
        {
            break;
        }
        //Goal,未满足，则重新计算
        if(IsSatisfyCon(pknowledge))
        {
           OnSatisfy(); 
        }

        m_LastCalGoalTime = TimeHelper::getCurrentTimestamp();

    }while (false);
}

void IGoal::OnSatisfy()
{
    //满足条件，则更新状态
    m_bSatisfy = true;
    m_OverdueTime = TimeHelper::getCurrentTimestamp() + m_GoalTimeOut;
}


bool IGoal::IsSatisfyCon(const AIKnowledge* pK) const
{
    for (auto con : m_vecConditions)
    {
        if (!con->IsSatisfy(pK->GetPlayer()))
        {
            return false;
        }
    }
    return true;
}

bool IGoal::AddCondition(IAICon* pCondition)
{
    if (nullptr == pCondition)
    {
        return false;
    }
    // 检查条件是否已经存在
    for (auto con : m_vecConditions)
    {
        if (con->GetId() == pCondition->GetId())
        {
            return false; // 条件已存在
        }
    }
    m_vecConditions.push_back(pCondition);
    return true;
}