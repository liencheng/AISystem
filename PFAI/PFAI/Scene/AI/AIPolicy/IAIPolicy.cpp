#include "Public.h"
#include "IAIPolicy.h"
#include "Utils/Utils.h"
#include "../AIBehavior/BehaviorFactory.h"


void IAIPolicy::Update(float fDeltaTime)
{
    if(IsBehaviorDirty() == true || m_pAIKnowledge.IsDirty())
    {
        ClearBehaviorDirty();
        m_pAIKnowledge.ClearDirty();

        UpdateView();
        UpdateDbg();
    }
}

void IAIPolicy::Init()
{
    InitBehaviorFromCfg();
}

void IAIPolicy::InitBehaviorFromCfg()
{
    int32_t nNpcDataId = m_pOwner->GetDataID();
    Table_NpcAIPolicyRoot * pRoot = TABLE_GET_BY_ID(Table_NpcAIPolicyRoot)(nNpcDataId);
    if(nullptr == pRoot)
    {
        LOG_ERROR("IAIPolicy::InitBehaviorFromCfg, nNpcDataId = " + std::to_string(nNpcDataId));
        return;
    }
    
    Table_NpcAIPolicy * pPolicy = TABLE_GET_BY_ID(Table_NpcAIPolicy)(pRoot->GetId());
    if(nullptr == pPolicy)
    {
        LOG_ERROR("IAIPolicy::InitBehaviorFromCfg, nNpcDataId = " + std::to_string(nNpcDataId));
        return;
    }

    std::string strBehaviorList = pPolicy->GetBehaviorList();
    std::vector<int32_t> vecBehaviorList = solar::StringUtils::SplitString(strBehaviorList);

    if(vecBehaviorList.empty() == true)
    {
        LOG_ERROR("IAIPolicy::InitBehaviorFromCfg vecBehaviorList.Empty, nNpcDataId = " + std::to_string(nNpcDataId));
        return;
    }

    for (auto & id : vecBehaviorList)
    {
        IBehavior * pBehavior = BehaviorFactory::Create(m_pOwner, id);
        if(nullptr == pBehavior)
        {
            LOG_ERROR("IAIPolicy::InitBehaviorFromCfg, NpcID = " + std::to_string(nNpcDataId) + ", id = " + std::to_string(id));
            continue;
        }
        AddBehavior(pBehavior);
        LOG_INFO("IAIPolicy::InitBehaviorFromCfg, NpcID = " + std::to_string(nNpcDataId) + ", id = " + std::to_string(id));
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