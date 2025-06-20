#pragma once
#include "IAICon.h"
#include "../../Obj/Obj_Char.h"

class AIConInCombat:public IAICon
{
public:
    AIConInCombat(const Table_NpcAICondition* pCon) :IAICon(pCon) {};
    ~AIConInCombat() = default;

public:
    virtual  bool IsSatisfy(Obj_Char* pOwner) override
    {
        MAYBE_DEBUG;
        
        return pOwner->IsInCombat();
    }
};
