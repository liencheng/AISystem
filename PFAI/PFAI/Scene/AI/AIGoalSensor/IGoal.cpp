#include "IGoal.h"
#include "../../../Public/Utils/Time.h"




IGoal::IGoal(int32_t nCfgId)
{
    m_CfgId = nCfgId;
    Init();
}

void IGoal::Init()
{
    //init data from cfg Table_Goal
}

void IGoal::OnUpdate(const AIKnowledge* pknowledge)
{
    do{
        //已满足且未过期，则不更新
        if(IsGoalSatisfy() && !IsOverdue())
            break;
        //Goal,超时了，则重新计算
        if(IsGoalSatisfy() && IsOverdue())
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
    SetOverdueTime(TimeHelper::getCurrentTimestamp() + m_GoalLifetime);
}


bool IGoal::IsSatisfyCon(const AIKnowledge* pK) const
{
    for (auto con : m_vecConditions)
    {
        if (!con->IsSatisfy(pK->m_pPlayer))
        {
            return false;
        }
    }
    return true;
}