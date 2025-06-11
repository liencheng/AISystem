#include "AIKnowledge.h"


void AIKnowledge::InitGoals()
{
    // Clear existing goals
    m_vecGoals.clear();
    static_assert(false, "AIKnowledge::InitGoals() should be init from config");
}

void AIKnowledge::Update()
{
    UpdateGoals();
    UpdateSignals();
}

bool AIKnowledge::AddGoals(IGoal* pGoal)
{
    // Check if the goal is already in the list
    for (const auto& goal : m_vecGoals)
    {
        if (goal->GetGoalType() == pGoal->GetGoalType())
        {
            return false; // Goal already exists
        }
    }
    m_vecGoals.push_back(pGoal);
    MarkDirty();
    return true;
}

bool AIKnowledge::DelGoals(IGoal* pGoal)
{
    for (auto it = m_vecGoals.begin(); it != m_vecGoals.end(); ++it)
    {
        if ((*it)->GetGoalType() == pGoal->GetGoalType())
        {
            m_vecGoals.erase(it); // Remove the goal from the list
            MarkDirty();
            return true;
        }
    }
    return false; // Goal not found
}



bool AIKnowledge::ProduceSignal(const AISignal& signal)
{
    // Check if the signal is already in the list
    for (const auto& existingSignal : m_vecSignals)
    {
        if (existingSignal.GetSignalType() == signal.GetSignalType())
        {
            return false; // Signal already exists
        }
    }
    m_vecSignals.push_back(signal);
    MarkDirty();
    return true;
    
}

bool AIKnowledge::ConsumeSignal(const AISignal& signal)
{
    // Check if the signal is in the list
    for (auto it = m_vecSignals.begin(); it != m_vecSignals.end(); ++it)
    {
        if (it->GetSignalType() == signal.GetSignalType())
        {
            MarkDirty();
            m_vecSignals.erase(it); // Remove the signal from the list
            return true;
        }
    }
    return false; // Signal not found
}


void AIKnowledge::UpdateGoals()
{
    // Iterate through the goals and update them
    for (auto& goal : m_vecGoals)
    {
        goal->OnUpdate(this);
    }
}

void AIKnowledge::UpdateSignals()
{
    // Iterate through the signals and check if they are expired
    for (auto it = m_vecSignals.begin(); it != m_vecSignals.end();)
    {
        if (it->isExpired())
        {
            MarkDirty();
            it = m_vecSignals.erase(it); // Remove expired signal
        }
        else
        {
            ++it; // Move to the next signal
        }
    }
}



