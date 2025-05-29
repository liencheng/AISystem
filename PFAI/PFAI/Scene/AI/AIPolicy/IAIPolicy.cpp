#include "IAIPolicy.h"



bool IAIPolicy::AddBehavior(IBehavior * pBehavior)
{
    if (pBehavior == nullptr)
    {
        return false;
    }
    // Check if the behavior already exists in the policy
    for (const auto& behavior : m_vecBehavior)
    {
        if (behavior->GetId() == pBehavior->GetId())
        {
            return false; // Behavior already exists
        }
    }
    m_vecBehavior.push_back(pBehavior);
    return true;
}


IDbgNess * IAIPolicy::GetDbgNode(int32_t id) const
{
    for (const auto& dbgNode : m_vecDbgNodes)
    {
        if (dbgNode->DbgGetId() == id)
        {
            return dbgNode;
        }
    }
    return nullptr; // Not found
}