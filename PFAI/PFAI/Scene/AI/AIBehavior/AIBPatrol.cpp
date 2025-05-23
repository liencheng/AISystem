#include "AIBPatrol.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../AIBehavior/IBehavior.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../../Obj/Obj_Char.h"

void AIBPatrol::OnStart()
{
    
}

void AIBPatrol::OnUpdate()
{
    IBehavior::OnUpdate();
    // Perform patrol logic
    if (m_bIsPatrolling)
    {
        // Move to the next patrol point
        m_Owner->Caskill(m_vecPatrolPoints[m_nPatrolPointIndex].x);
        m_nPatrolPointIndex = (m_nPatrolPointIndex + 1) % 5; // Loop through patrol points
    }
}

void AIBPatrol::OnEnd()
{
    SetBehaviorStatus(AIBehaviorStatus::ABS_End);
}

bool AIBPatrol::Interrupt()
{
    OnEnd();
}
