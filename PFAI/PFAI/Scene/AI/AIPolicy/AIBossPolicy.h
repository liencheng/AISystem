#pragma once
#include "IAIPolicy.h"

class AIBossPolicy: public IAIPolicy
{
public:
    AIBossPolicy(const Obj_Char *pOwner):IAIPolicy(pOwner){ };
public:
    virtual void Update(float fDeltaTime) override;
    virtual IBehavior* Decision() override;
private:
    virtual IBehavior* SelectBestBehavior()const override;
    
};
