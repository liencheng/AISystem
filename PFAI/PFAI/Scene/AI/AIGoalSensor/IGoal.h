#pragma once
#include <vector>

#include "../AICondition/IAICon.h"
#include "../AIKnowledge/AIKnowledge.h"

class IGoal
{
public:
    virtual void OnStart() = 0; // Called when the goal starts
    virtual void OnUpdate(const AIKnowledge * pknowledge);
    virtual void OnEnd() = 0; // Called when the goal ends

    bool         IsGoalSatisfy() const { return m_bIsSatisfy; } // Check if the goal is satisfied

protected:
    virtual bool IsSatisfyCon(const AIKnowledge *pKnowledge) const; // Check if the goal's conditions are satisfied

protected:
    std::vector<IAICon*> m_vecConditions; // List of conditions associated with the goal
    bool                 m_bIsSatisfy = false; // Flag indicating if the goal is satisfied
    time_t               m_OverdueTime = 0; // Time when the goal will expire
    int32_t              m_Id = 0;
    int32_t              m_Weight = 0; // Weight of the goal, used for prioritization
};
