#pragma once
#include "IAICon.h"
#include "../../Obj/Obj_Char.h"

class AIConInCombat:IAICon
{
public:
    AIConInCombat() = default;
    ~AIConInCombat() = default;

public:
    virtual  bool IsSatisfy(Obj_Char* pOwner) override
    {
        return pOwner->IsInCombat();
    }
};
