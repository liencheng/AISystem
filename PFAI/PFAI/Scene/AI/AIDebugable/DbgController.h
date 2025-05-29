#pragma once
#include "../AIPolicy/IAIPolicy.h"

class DbgController
{
public:
    DbgController(IAIPolicy * pAIPolicy):m_pAIPolicy((pAIPolicy)){}
    
    /*激活调试*/
    bool        DbgActiveCondtion(int32_t nDbgId);
    bool        DbgActiveSignal(int32_t nDbgId);
    bool        DbgActiveGoal(int32_t nDbgId);
    bool        DbgActiveBehavior(int32_t nDbgId);

    /*增加或者删除调试*/
    bool        DbgAddCondtion();
    bool        DbgDelCondtion();
    bool        DbgAddSignal();
    bool        DbgDelSignal();
    bool        DbgAddGoal();
    bool        DbgDelGoal();
    bool        DbgAddBehavior();
    bool        DbgDelBehavior();

    /*单步调试*/
    bool        DbgStepCondtion();


    /*获取调试信息*/
    bool        DbgGetVariableInfo();
private:
    IAIPolicy * m_pAIPolicy = nullptr; // AI策略
};
