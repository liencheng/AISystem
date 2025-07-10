#include "Public.h"
#include "AIKnowledge.h"
#include "Utils/Utils.h"
#include "../AIGoalSensor/IGoal.h"

AIKnowledge::AIKnowledge(Obj_Char *pChar)
{
	m_pOwner = pChar;
	m_pScene = m_pOwner->GetScene();
	m_bDirty = false; // Initialize dirty flag
	InitGoals(); // Initialize goals 

}

void AIKnowledge::InitGoals()
{
    // Clear existing goals
    m_vecGoals.clear();
    int32_t nNpcDataId = m_pOwner->GetDataID();
    Table_NpcAIPolicyRoot * pRoot = TABLE_GET_BY_ID(Table_NpcAIPolicyRoot)(nNpcDataId);
    if(nullptr == pRoot)
    {
        LOG_ERROR("AIKnowledge::InitGoals pRoot=nullptr, nNpcDataId = " + std::to_string(nNpcDataId));
        return;
    }
    
    Table_NpcAIPolicy * pPolicy = TABLE_GET_BY_ID(Table_NpcAIPolicy)(pRoot->GetId());
    if(nullptr == pPolicy)
    {
        LOG_ERROR("AIKnowledge::InitGoals pPolicy=nullptr, nNpcDataId = " + std::to_string(nNpcDataId));
        return;
    }

    std::string strGoalList = pPolicy->GetGoalSensorList();
    std::vector<int32_t> vecGoalList = solar::StringUtils::SplitString(strGoalList);

    if(vecGoalList.empty() == true)
    {
        LOG_ERROR("AIKnowledge::InitGoals, nNpcDataId = " + std::to_string(nNpcDataId) + ", strGoalList.empty() == true");
        return;
    }

    for (auto & id : vecGoalList)
    {
        IGoal goal(id);
        AddGoals(goal);
        LOG_INFO("AIKnowledge::InitGoals, nNpcDataId = " + std::to_string(nNpcDataId) + ", strGoalList.size() = " + std::to_string(vecGoalList.size()));
        MarkDirty();
    }
}

void AIKnowledge::Update()
{
    UpdateGoals();
    UpdateSignals();
}

bool AIKnowledge::AddGoals(IGoal& pGoal)
{
    // Check if the goal is already in the list
    for (const auto& goal : m_vecGoals)
    {
        if (goal.GetGoalType() == pGoal.GetGoalType())
        {
            return false; // Goal already exists
        }
    }
    m_vecGoals.push_back(pGoal);
    MarkDirty();
    return true;
}

bool AIKnowledge::DelGoals(IGoal& pGoal)
{
    for (auto it = m_vecGoals.begin(); it != m_vecGoals.end(); ++it)
    {
        if ((it)->GetGoalType() == pGoal.GetGoalType())
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
        goal.OnUpdate(this);
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



