/*
 * Copyright (C) 2023-2024  PFAI
 * Goals的完成完成提交依赖于Condition 
 * 注：Goal应该不需要用多态，因为GoaL具体执行逻辑依赖于配置的Condition
 */

#pragma once
#include <vector>
#include <cstdint>

#include "../AICondition/IAICon.h"
#include "../AIDebugable/IDbgNess.h"


class AIKnowledge; // Forward declaration of AIKnowledge class

enum class E_AIGoalType
{
    G_None = 0,
    G_MoveTo,
    G_Chat,
    G_Attack,
    G_Follow,
};

class IGoal:IDbgNess
{

public:
    
    IGoal(int32_t cfgid);
    virtual ~IGoal() {}

    virtual void Init(int32_t nCfgId);

    virtual void OnStart() {};
    virtual void OnUpdate(const AIKnowledge* pknowledge);
    virtual void OnEnd() {};
    virtual DbgInfo FetchDbgInfo() const override {
        return DbgInfo();
    };

    bool         IsGoalSatisfy() const { MAYBE_DEBUG;  return m_bSatisfy; } // Check if the goal is satisfied
    int32_t      GetId() const { return m_Id; } // Get the ID of the goal
    int32_t      GetWeight() const { return m_CfgWeight; } // Get the weight of the goal
    bool         AddCondition(IAICon *pCondition); // Add a condition to the goal
    E_AIGoalType GetGoalType() const { return m_EGaolType; } // Get the type of the goal


protected:
    virtual bool IsSatisfyCon(const AIKnowledge *pKnowledge) const; // Check if the goal's conditions are satisfied

protected:
    int32_t              m_Id = 0;
    bool                 m_bSatisfy = false; // Flag indicating if the goal is satisfied
    time_t               m_OverdueTime = 0; // Time when the goal will expire
    int32_t              m_LastCalGoalTime = 0; //  上次计算目标时间
    std::vector<IAICon*> m_vecConditions; // List of conditions associated with the goal

    bool                 IsTimeOut() const; // Check if the goal has expired
    bool                 InCalGoalCD() const; // Check if it's within the goal's time interval
    void                 Reset(); // Reset the goal to its initial state
    void                 OnSatisfy(); // Handle the satisfaction of the goal


    //Goal的权重从10000开始，数值越大优先级越高
    E_AIGoalType         m_EGaolType = E_AIGoalType::G_None; // Type of the goal
    int32_t              m_CfgId;
    int32_t              m_CfgWeight = 0; // Weight of the goal, used for prioritization
    int32_t              m_CfgCalGoalInterval = 0; // Interval for recalculating the goal
    int32_t              m_CfgGoalTimeOut = 0; // Duration for recalculating the goal
};
