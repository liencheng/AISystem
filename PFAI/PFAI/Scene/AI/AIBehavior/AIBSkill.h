#pragma once
#include "IBehavior.h"

class AIBSkill:public IBehavior
{
public:
   AIBSkill(Obj_Char * pOwner, const Table_NpcAIBehavior * pBehavior):IBehavior(pOwner, pBehavior){  }
   virtual ~AIBSkill(){};
private:
   int32_t m_nSkillId = -1; // Skill ID
public:
   virtual void OnStart() override;
   virtual void OnUpdate() override;
   virtual void OnEnd(E_AIBehaviorStatus result) override;

};
