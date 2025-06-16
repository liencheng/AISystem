#pragma once
#include <vector>
#include "Public.h"
#include "AIBehaviorInfo.h"

#include "../GameDfine_AI/AIDefine.h"
#include "../AICondition/IAICon.h"
#include "../../Obj/Obj_Char.h"


//todo: 可以考虑把Condtion从行为类中剥离出来， 用于多个行为类公用，以提供性能
class IBehavior
{
public:
    IBehavior(Obj_Char * owner, const Table_NpcAIBehavior * pBehavior):
    m_Owner(owner),
    m_pBehavior(pBehavior)
    {}
protected:
    //AIBehaviorInfo              m_behaviorInfo; // Pointer to the behavior information
    Obj_Char *                  m_Owner = nullptr; // Pointer to the owner of the behavior
    const Table_NpcAIBehavior * m_pBehavior = nullptr; // Pointer to the behavior information table
    std::vector<IAICon>       m_vecConditions; // List of conditions associated with the behavior
    std::vector<const AISignal*>     m_vecSignals; // List of signals associated with the behavior
    std::vector<const IGoal*>       m_vecGoals; // List of goals associated with the behavior
private:
    time_t              m_LastExecuteTime = 0; // The last time the behavior was executed
    int32_t             m_nId = -1; // Unique ID for the behavior
    int32_t             m_nPrority = 0; // Priority of the behavior
    E_AIBehaviorStatus    m_eBehaviorStatus = E_AIBehaviorStatus::ABS_None; // The current status of the behavior
public:
    void                SetLastExecuteTime(float time) { m_LastExecuteTime = time; } // Set the last execute time
    time_t              GetLastExecuteTime() const { return m_LastExecuteTime; } // Get the last execute time
    void                SetBehaviorStatus(E_AIBehaviorStatus status) { m_eBehaviorStatus = status; } // Set the behavior status
    E_AIBehaviorStatus    GetBehaviorStatus() const { return m_eBehaviorStatus; } // Get the behavior status

    bool                TimeOut()const{return false;}

public:
    int32_t GetId() const { return m_nId; } // Get the ID of the behavior
    int32_t GetWeightOfPriority() const { return m_nPrority; } // Get the priority of the behavior
    int32_t GetWeightOfSignal() const;
    int32_t GetWeightOfGoal() const; // Get the weight of a goal based on knowledge
    int32_t GetFinalWeight() const; // Get the final weight of the behavior based on priority, signal, and goal weights


    bool IsInCD() const { return false; } // Check if the behavior is in cooldown

    
    
    
public:
    virtual  bool IsSatisfyCondition(const AIKnowledge * pknowledge); // Check if the conditions are satisfied
    virtual  void OnStart() = 0; // Called when the behavior starts
    virtual  void OnUpdate()
    {
        m_LastExecuteTime = 0;
    }
    virtual  void OnEnd(E_AIBehaviorStatus result) = 0; // Called when the behavior ends
    virtual  bool CanInterrupt() = 0; // 是否可以被打断
    virtual  bool Interrupt() =0; // 打断行为
};
