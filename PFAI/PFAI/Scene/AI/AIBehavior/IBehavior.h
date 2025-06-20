#pragma once
#include <vector>
#include "Public.h"
#include "AIBehaviorInfo.h"

#include "../GameDfine_AI/AIDefine.h"
#include "../AICondition/IAICon.h"
#include "../../Obj/Obj_Char.h"
#include "Utils/GenId.h"
#include <Utils/Time.h>


//todo: 可以考虑把Condtion从行为类中剥离出来， 用于多个行为类公用，以提供性能
class IBehavior
{
public:
    IBehavior(Obj_Char* owner, const Table_NpcAIBehavior* pBehavior) :
        m_Owner(owner),
        m_pBehavior(pBehavior){
		SOL_ASSERT(m_pBehavior != nullptr, "IBehavior::IBehavior, pBehavior is null");
        m_nId =  gGenBehaviorId.generate();
        m_nPrority = m_pBehavior->GetProprity();
		m_fCDs = m_pBehavior->GetCD();
		m_nTimeout = m_pBehavior->GetTimeout();

        Init(pBehavior);
    }
    
    virtual ~IBehavior();
protected:
    //AIBehaviorInfo              m_behaviorInfo; // Pointer to the behavior information
    Obj_Char* m_Owner = nullptr; // Pointer to the owner of the behavior
    const Table_NpcAIBehavior* m_pBehavior = nullptr; // Pointer to the behavior information table
    std::vector<IAICon*>       m_vecConditions; // List of conditions associated with the behavior
    //20250620暂时废弃****
    std::vector<const AISignal*>     m_vecSignals; // List of signals associated with the behavior
	//20250620暂时废弃****
    std::vector<const IGoal*>       m_vecGoals; // List of goals associated with the behavior
private:
    int32_t             m_nId = -1; // Unique ID for the behavior
    int32_t             m_nPrority = 0; // Priority of the behavior
	float               m_fCDs = 0; // Cooldown time in seconds
    time_t              m_LastExecuteTime = 0; // The last time the behavior was executed
    E_AIBehaviorStatus    m_eBehaviorStatus = E_AIBehaviorStatus::ABS_Ready; // The current status of the behavior
	uint64_t             m_nTimeout = 0; // Timeout for the behavior in ms
	uint64_t 		    m_nStartTime = 0; // The time when the behavior started, used for timeout calculations
public:
    void                SetLastExecuteTime(float time) { m_LastExecuteTime = time; } // Set the last execute time
    time_t              GetLastExecuteTime() const { return m_LastExecuteTime; } // Get the last execute time
    void                SetBehaviorStatus(E_AIBehaviorStatus status) { m_eBehaviorStatus = status; } // Set the behavior status
    E_AIBehaviorStatus    GetBehaviorStatus() const { return m_eBehaviorStatus; } // Get the behavior status


public:
    void    Init(const Table_NpcAIBehavior * pBCfg);
    int32_t GetId() const { return m_nId; } // Get the ID of the behavior
    int32_t GetWeightOfPriority() const { return m_nPrority; } // Get the priority of the behavior
	//todo： desperate
    int32_t GetWeightOfSignal() const;
	//todo： desperate
    int32_t GetWeightOfGoal() const; // Get the weight of a goal based on knowledge
    int32_t GetFinalWeight() const; // Get the final weight of the behavior based on priority, signal, and goal weights

    bool IsInCD() const { 
        return ((m_LastExecuteTime > 0) && 
            (TimeHelper::getCurrentTimestamp() - m_LastExecuteTime > m_fCDs)); 
    } 
    bool TimeOut()const { 
        return m_nTimeout >0 && (TimeHelper::getCurrentTimestamp() * 1000 - m_nStartTime > m_nTimeout);
    }


public:
    virtual  bool IsSatisfyCondition(const AIKnowledge* pknowledge); // Check if the conditions are satisfied
    virtual  void OnUpdate()
    {
        m_LastExecuteTime = 0;
    }
    virtual  void OnStart() { m_nStartTime = TimeHelper::getCurrentTimestamp() * 1000; };
    virtual  void OnEnd(E_AIBehaviorStatus result) {};
    virtual  bool CanInterrupt() { return false; };
    virtual  bool Interrupt() { return false; };
};
