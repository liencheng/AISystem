#include "AIBSkill.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../AIBehavior/IBehavior.h"
#include "../AICondition/IAICon.h"
#include "Utils/Logger.h"

void AIBSkill::OnStart()
{
	IBehavior::OnStart();
	LOG_INFO("AIBSkill::OnStart, SkillId:{}", m_nSkillId);
}

void AIBSkill::OnUpdate()
{
    IBehavior::OnUpdate();

    if(TimeOut())
    {
        OnEnd(E_AIBehaviorStatus::ABS_TimeOut);
    }
    
    m_Owner->Caskill(m_nSkillId);
	LOG_INFO("AIBSkill::OnUpdate, SkillId:{}", m_nSkillId);
    // Update the skill behavior
    OnEnd(E_AIBehaviorStatus::ABS_Succ);
}

void AIBSkill::OnEnd(E_AIBehaviorStatus result)
{
    IBehavior::OnEnd(result);
    SetBehaviorStatus(result);
	LOG_INFO("AIBSkill::OnEnd, SkillId:{}, Result:{}", m_nSkillId, static_cast<int>(result));
}
