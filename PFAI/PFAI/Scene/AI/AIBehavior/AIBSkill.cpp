#include "AIBSkill.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../AIBehavior/IBehavior.h"
#include "../AICondition/IAICon.h"

void AIBSkill::OnStart()
{
}

void AIBSkill::OnUpdate()
{
    IBehavior::OnUpdate();

    if(TimeOut())
    {
        OnEnd(E_AIBehaviorStatus::ABS_TimeOut);
    }
    
    m_Owner->Caskill(m_nSkillId);
    // Update the skill behavior
    OnEnd(E_AIBehaviorStatus::ABS_Succ);
}

void AIBSkill::OnEnd(E_AIBehaviorStatus result)
{
    SetBehaviorStatus(result);
}
