#pragma once
#include <cstdint>

#include "IAICon.h"
#include "../../../Public/DataDefine.h"

class AIConGotoPoint:public IAICon
{
public:
    AIConGotoPoint(const Table_NpcAICondition* pCon) :IAICon(pCon)
    {
        Init();
    }

    virtual bool IsSatisfy(Obj_Char* pOwner) override
    {
        MAYBE_DEBUG;
        
        // Check if the character is at the target position
        //return pOwner->GetPosition() == m_TargetPos;
        return false;
    }

    void Init()
    {
        //todo:init TargetPos
    }

private:
    ScenePos    m_TargetPos; // Target position to go to
    float       m_Radius = 0.0f;
};
