#pragma once
#include "IAIPolicy.h"

class Obj_Char; // Forward declaration of Obj_Char class

class AIBossPolicy: public IAIPolicy
{
public:
    AIBossPolicy(Obj_Char *pOwner):IAIPolicy(pOwner){ };
public:
    virtual void Update(float fDeltaTime) override;
    virtual IBehavior* Decision() override;
private:
    virtual IBehavior* SelectBestBehavior()const override;
    
};
