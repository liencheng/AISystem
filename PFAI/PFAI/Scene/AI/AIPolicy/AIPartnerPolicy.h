#pragma once
#include "IAIPolicy.h"

class AIPartnerPolicy: IAIPolicy
{
public:
    AIPartnerPolicy(){};
public:
    virtual void Update(float fDeltaTime) override;
    virtual bool AddBehavior(IBehavior * pBehavior) override;
    virtual bool Decision() override;
    
};
