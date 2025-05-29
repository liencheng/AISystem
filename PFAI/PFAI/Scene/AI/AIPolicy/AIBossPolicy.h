#pragma once
#include "IAIPolicy.h"

class AIBossPolicy:IAIPolicy
{
public:
    AIBossPolicy(){};
public:
    virtual void Update(float fDeltaTime) override;
    virtual IBehavior* Decision() override;
private:
    virtual IBehavior* SelectBestBehavior()const override;
    
};
