#include "AIKnowledge.h"

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
    return true;
}


bool AIKnowledge::ReceiveSignal(const AISignal& signal)
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
    return true;
    
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
            it = m_vecSignals.erase(it); // Remove expired signal
        }
        else
        {
            ++it; // Move to the next signal
        }
    }
}

void AIKnowledge::Update()
{
    UpdateGoals();
    UpdateSignals();
}


