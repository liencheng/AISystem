#include "IBehavior.h"
#include "Utils/Utils.h"
#include "../AICondition/AIConFactory.h"
#include "../AIKnowledge/AIKnowledge.h"


IBehavior::~IBehavior()
{
	// Clean up conditions
	for (auto condition : m_vecConditions)
	{
		delete condition; // Assuming IAIcon is not a pointer, so we delete the reference
	}
	m_vecConditions.clear();
}

void IBehavior::Init(const Table_NpcAIBehavior* pBCfg)
{
	SOL_ASSERT(pBCfg != nullptr, "IBehavior::Init, pBCfg is null");
	m_nId = pBCfg->GetId();
	m_fCDs = pBCfg->GetCD();
	m_nTimeout = pBCfg->GetTimeout();
	m_nPrority = pBCfg->GetProprity();
	// Initialize conditions
	std::string conditionList = pBCfg->GetConditionList();
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
					m_vecConditions.push_back(pAICon);
				}
				else
				{
					LOG_ERROR("IBehavior::Init, CreateAICondition failed, CfgId:{}, ConditionId:{}", m_nId, con);
				}
			}
			else
			{
				LOG_ERROR("IBehavior::Init, ConditionCfg is null, CfgId:{}, ConditionId:{}", m_nId, con);
			}
		}
	}
}


bool IBehavior::IsSatisfyCondition(const AIKnowledge* pKnowledge)
{
    for (auto condition : m_vecConditions)
    {
        if (!condition->IsSatisfy(pKnowledge->GetPlayer()))
        {
            return false;
        }
    }
    return true;
}


int32_t IBehavior::GetFinalWeight() const
{
    return m_nPrority;
}

int32_t IBehavior::GetWeightOfGoal() const
{
    // 遍历所有目标,选择一个最大的目标权重返回
    int32_t maxWeight = 0;
    for(auto goal : m_vecGoals)
    {
        if(goal->IsGoalSatisfy())
        {
            int32_t nW = goal->GetWeight();
            if(nW > maxWeight)
            {
                maxWeight = nW;
            }
        }
    }
    return maxWeight;
}

int32_t IBehavior::GetWeightOfSignal() const
{
    // 遍历所有信号,选择一个最大的信号权重返回
    int32_t nMaxWeight = 0;
    for(auto signal : m_vecSignals)
    {
        if(!signal->isExpired())
        {
            int32_t nW =  signal->GetWeight();
            if(nW > nMaxWeight)
            {
                nMaxWeight = nW;
            }
        }
    }
    return nMaxWeight;
}


/*
    bool IBehavior:: IsInCD() const 
    { 
        return ((m_LastExecuteTime > 0) && 
            (TimeHelper::getCurrentTimestamp() - m_LastExecuteTime > m_fCDs)); 
    } 
*/
    bool IBehavior:: TimeOut()const { 
        return m_nTimeout >0 && (TimeHelper::getCurrentTimestamp() * 1000 - m_nStartTime > m_nTimeout);
    }
