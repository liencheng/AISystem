#pragma once
#include "IBehavior.h"

class AIBSkill:IBehavior
{
private:
   int32_t m_nSkillId = -1; // Skill ID
public:
   virtual void OnStart() override;
   virtual void OnUpdate() override;
   virtual void OnEnd() override;
    
};
