#include "IBehavior.h"


bool IBehavior::IsSatisfyCondition(const AIKnowledge* pKnowledge)
{
    for (auto condition : m_vecConditions)
    {
        if (!condition.IsSatisfy(pKnowledge->GetPlayer()))
        {
            return false;
        }
    }
    return true;
}


int32_t IBehavior::GetFinalWeight() const
{
    return GetWeightOfGoal() + GetWeightOfPriority() + GetWeightOfSignal();
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


