#include "AIBSkill.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../AIBehavior/IBehavior.h"
#include "../AICondition/IAICon.h"

void AIBSkill::OnStart()
{
    // Initialize the skill behavior
}

void AIBSkill::OnUpdate()
{
    IBehavior::OnUpdate();
    m_Owner->Caskill(m_nSkillId);
    // Update the skill behavior
    OnEnd();
}

void AIBSkill::OnEnd()
{
    SetBehaviorStatus(AIBehaviorStatus::ABS_End);
}
