#include "Public.h"
#include "IAIPolicy.h"


void IAIPolicy::Update(float fDeltaTime)
{
    if(IsBehaviorDirty() == true || m_pAIKnowledge->IsDirty())
    {
        ClearBehaviorDirty();
        m_pAIKnowledge->ClearDirty();

        UpdateView();
        UpdateDbg();
    }
}

void IAIPolicy::Init()
{
	// Initialize AIKnowledge if it is not already initialized
	if (m_pAIKnowledge == nullptr)
	{
		m_pAIKnowledge = new AIKnowledge();
		if (m_pAIKnowledge)
		{
			m_pAIKnowledge->Init(m_pOwner);
		}
		else
		{
			LOG_ERROR("Failed to create AIKnowledge instance.");
		}
	}
	// Initialize behaviors if needed
	for (auto& behavior : m_vecBehavior)
	{
		if (behavior)
		{
			behavior->Init();
		}
	}
}

void IAIPolicy::UpdateView()
{
   static_assert(false, "need update view");
}

void IAIPolicy::UpdateDbg()
{
    static_assert(false, "need update dbg");
    //需要
}


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
    MarkBehaviorDirty();
    return true;
}

bool IAIPolicy::DelBehavior(IBehavior * pBehavior)
{
    for (auto it = m_vecBehavior.begin(); it != m_vecBehavior.end(); ++it)
    {
        if ((*it)->GetId() == pBehavior->GetId())
        {
            m_vecBehavior.erase(it);
            MarkBehaviorDirty();
            return true;
        }
    }
    return false;
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


bool IAIPolicy::AddDbgNode(IDbgNess * pDbgNode)
{
    if (pDbgNode == nullptr)
    {
        return false;
    }
    // Check if the dbgNode already exists in the policy
    for (const auto& dbgNode : m_vecDbgNodes)
    {
        if (dbgNode->DbgGetId() == pDbgNode->DbgGetId())
        {
            return false; // DbgNode already exists
        }
    }
    m_vecDbgNodes.push_back(pDbgNode);
    return true;
}

bool IAIPolicy::DelDbgNode(IDbgNess * pDbgNode)
{
    for (auto it = m_vecDbgNodes.begin(); it != m_vecDbgNodes.end(); ++it)
    {
        if ((*it)->DbgGetId() == pDbgNode->DbgGetId())
        {
            m_vecDbgNodes.erase(it);
            return true;
        }
    }
    return false;
}