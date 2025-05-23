#pragma once
#include "AIBehaviorInfo.h"
#include "../GameDfine_AI/AIDefine.h"
#include <vector>

#include "../../Obj/Obj_Char.h"
#include "../AICondition/IAICon.h"

//todo: 可以考虑把Condtion从行为类中剥离出来， 用于多个行为类公用，以提供性能
class IBehavior
{
public:
    IBehavior(Obj_Char * owner):m_Owner(owner){}
    IBehavior(Obj_Char * owner, std::vector<IAICon *> vecCondition):m_Owner(owner)
    {
        for (auto condition : vecCondition)
        {
            m_vecConditions.push_back(condition);
        }
    }
protected:
    AIBehaviorInfo              m_behaviorInfo; // Pointer to the behavior information
    std::vector<IAICon *>       m_vecConditions; // List of conditions associated with the behavior
    Obj_Char *                  m_Owner = nullptr; // Pointer to the owner of the behavior
private:
    time_t              m_LastExecuteTime = 0; // The last time the behavior was executed
    int32_t             m_nId = -1; // Unique ID for the behavior
    int32_t             m_nPrority = 0; // Priority of the behavior
    AIBehaviorStatus    m_eBehaviorStatus = AIBehaviorStatus::ABS_None; // The current status of the behavior
public:
    void                SetLastExecuteTime(float time) { m_LastExecuteTime = time; } // Set the last execute time
    time_t              GetLastExecuteTime() const { return m_LastExecuteTime; } // Get the last execute time
    void                SetBehaviorStatus(AIBehaviorStatus status) { m_eBehaviorStatus = status; } // Set the behavior status
    AIBehaviorStatus    GetBehaviorStatus() const { return m_eBehaviorStatus; } // Get the behavior status

public:
    int32_t GetId() const { return m_nId; } // Get the ID of the behavior
    int32_t GetPriority() const { return m_nPrority; } // Get the priority of the behavior
    bool IsInCD() const { return false; } // Check if the behavior is in cooldown

    
    
    
public:
    virtual  bool IsSatisfyCondition(); // Check if the conditions are satisfied
    virtual  void OnStart() = 0; // Called when the behavior starts
    virtual  void OnUpdate()
    {
        m_LastExecuteTime = 0;
    }
    virtual  void OnEnd() = 0; // Called when the behavior ends
    virtual  bool CanInterrupt() = 0; // 是否可以被打断
    virtual  bool Interrupt() =0; // 打断行为
};
