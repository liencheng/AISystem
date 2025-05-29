#include "DbgController.h"
#include "DbgInfo.h"

bool DbgController::DbgActiveCondtion(int32_t nDbgId)
{
    if (m_pAIPolicy)
    {
        IDbgNess * pNode =  m_pAIPolicy->GetDbgNode(nDbgId);
        if(nullptr != pNode) pNode->DbgSetEnable();
    }
    return false;
}

bool DbgController::DbgActiveSignal(int32_t nDbgId)
{
    if (m_pAIPolicy)
    {
        IDbgNess * pNode =  m_pAIPolicy->GetDbgNode(nDbgId);
        if(nullptr != pNode) pNode->DbgSetEnable();
    }
    return false;
}
bool DbgController::DbgActiveGoal(int32_t nDbgId)
{
    if (m_pAIPolicy)
    {
        IDbgNess * pNode =  m_pAIPolicy->GetDbgNode(nDbgId);
        if(nullptr != pNode) pNode->DbgSetEnable();
    }
    return false;
}
bool DbgController::DbgActiveBehavior()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgActiveBehavior();
    }
    return false;
}
bool DbgController::DbgAddCondtion()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->AddBehavior()
    }
    return false;
}
bool DbgController::DbgDelCondtion()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgDelCondtion();
    }
    return false;
}
bool DbgController::DbgAddSignal()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgAddSignal();
    }
    return false;
}
bool DbgController::DbgDelSignal()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgDelSignal();
    }
    return false;
}
bool DbgController::DbgAddGoal()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgAddGoal();
    }
    return false;
}
bool DbgController::DbgDelGoal()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgDelGoal();
    }
    return false;
}
bool DbgController::DbgAddBehavior()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgAddBehavior();
    }
    return false;
}
bool DbgController::DbgDelBehavior()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgDelBehavior();
    }
    return false;
}
bool DbgController::DbgStepCondtion()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgStepCondtion();
    }
    return false;
}
bool DbgController::DbgGetVariableInfo()
{
    if (m_pAIPolicy)
    {
        return m_pAIPolicy->DbgGetVariableInfo();
    }
    return false;
}
