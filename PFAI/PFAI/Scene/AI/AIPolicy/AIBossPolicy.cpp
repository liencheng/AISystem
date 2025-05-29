#include "AIBossPolicy.h"

#include <map>


void AIBossPolicy::Update(float fDeltaTime)
{
    do
    {
        // 如果当前行为已经结束，则结束当前行为
        if(m_pCurrentBehavior!=nullptr
            && m_pCurrentBehavior->GetBehaviorStatus()>=E_AIBehaviorStatus::ABS_End)
        {
            m_pCurrentBehavior = nullptr;
            break;
        }
        if(m_pCurrentBehavior!=nullptr)
        {
            m_pCurrentBehavior->OnUpdate();
        }
        //更新操作
        Decision();
    }while (false);
}

IBehavior* AIBossPolicy::Decision()
{
    // Implement the decision-making logic for the boss policy
    // 1. 选择最优行为
    IBehavior * pBehavior = SelectBestBehavior();
    if (nullptr == pBehavior)
    {
        return nullptr;
    }
    // 2. 执行行为
    if (pBehavior != m_pCurrentBehavior)
    {
    //3. 打断行为    
        if (nullptr != m_pCurrentBehavior)
        {
            m_pCurrentBehavior->Interrupt();
        }
        m_pCurrentBehavior = pBehavior;
        m_pCurrentBehavior->OnStart();
    }
    m_pCurrentBehavior->OnUpdate();
    return m_pCurrentBehavior;
}

IBehavior * AIBossPolicy::SelectBestBehavior() const
{
    /* Step:
     * 如果没有正在执行的行为，则选择一个行为来执行
     * 如果有正在执行的行为，则检查是否可打断，如果不可打断，则返回
     * 如果可打断，则选择一个优先级更高的行为并打断当前行为
     * 如果没有优先级更高的行为，则继续执行当前行为
     * 如果存在多个优先级相同的行为，则随机选择一个执行
     */

    //step1: 不可打断
    if(nullptr != m_pCurrentBehavior && m_pCurrentBehavior->CanInterrupt() == false)
    {
        return m_pCurrentBehavior;
    }

    //step2: 找到一个优先级更高的行为
    int32_t nCurBehaviorId = -1;
    int32_t nCurBehaviorPriority = -1;
    if (nullptr != m_pCurrentBehavior)
    {
        nCurBehaviorId = m_pCurrentBehavior->GetId();
        nCurBehaviorPriority = m_pCurrentBehavior->GetFinalWeight();
    }
    int32_t nMaxBehaviorPriority = nCurBehaviorPriority;
    std::vector<IBehavior *> priorityBehaviors;    // 记录优先级相同的行为
    for (auto behavior : m_vecBehavior)
    {
        //同一个行为不能重复添加
        if(behavior->GetId() == nCurBehaviorId)
        {
            continue;
        }
        // 检查行为是否在冷却中
        if(behavior->IsInCD())
        {
            continue;
        }
        // 检查行为是否满足条件
        if (!behavior->IsSatisfyCondition(m_pAIKnowledge))
        {
            continue;
        }

        int32_t nFinalWeight = behavior->GetFinalWeight();

        if(nFinalWeight <= nCurBehaviorPriority)
        {
            continue;
        }
        // 找到优先级更高的行为
        if(nMaxBehaviorPriority < nFinalWeight)
        {
            priorityBehaviors.clear();
            priorityBehaviors.push_back(behavior);
            nMaxBehaviorPriority = nFinalWeight;
        }
        // 如果优先级相同，则加入到列表中
        else if(nMaxBehaviorPriority == nFinalWeight)
        {
            priorityBehaviors.push_back(behavior);
        }
    }

    //step3: 如果没有优先级更高的行为，则继续执行当前行为
    if(priorityBehaviors.empty())
    {
        return m_pCurrentBehavior;
    }
    //step4: 如果有优先级更高的行为，则随机选择一个执行
    int32_t nRandomIndex = rand() % priorityBehaviors.size();
    IBehavior * pBehavior = priorityBehaviors[nRandomIndex];
    return pBehavior;
}