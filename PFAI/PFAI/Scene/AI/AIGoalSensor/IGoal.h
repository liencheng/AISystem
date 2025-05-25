#pragma once
#include <vector>
#include <cstdint>

#include "../AICondition/IAICon.h"
#include "../AIKnowledge/AIKnowledge.h"

class IGoal
{

public:

    IGoal(int32_t cfgid);
    virtual ~IGoal() {}

    virtual void Init();

    virtual void OnStart() = 0; // Called when the goal starts
    virtual void OnUpdate(const AIKnowledge * pknowledge);
    virtual void OnEnd() = 0; // Called when the goal ends

    bool         IsGoalSatisfy() const { return m_bSatisfy; } // Check if the goal is satisfied
    int32_t      GetId() const { return m_Id; } // Get the ID of the goal
    int32_t      GetWeight() const { return m_Weight; } // Get the weight of the goal



protected:
    virtual bool IsSatisfyCon(const AIKnowledge *pKnowledge) const; // Check if the goal's conditions are satisfied

protected:
    bool                 m_bSatisfy = false; // Flag indicating if the goal is satisfied
    time_t               m_OverdueTime = 0; // Time when the goal will expire
    int32_t              m_LastCalGoalTime = 0; //  上次计算目标时间
    std::vector<IAICon*> m_vecConditions; // List of conditions associated with the goal

    void                 SetSatisfy(bool bIsSatisfy); // Set the satisfaction status of the goal
    void                 SetOverdueTime(time_t t); // Set the time when the goal will expire
    bool                 IsOverdue() const; // Check if the goal has expired
    bool                 InCalGoalCD() const; // Check if it's within the goal's time interval
    void                 Reset(); // Reset the goal to its initial state
    void                 OnSatisfy(); // Handle the satisfaction of the goal


    int32_t              m_CfgId;
    int32_t              m_Id = 0;
    //Goal的权重从10000开始，数值越大优先级越高
    int32_t              m_Weight = 0; // Weight of the goal, used for prioritization
    int32_t              m_CalGoalInterval = 0; // Interval for recalculating the goal
    int32_t              m_GoalLifetime = 0; // Duration for recalculating the goal

};
