#pragma once
#include <cstdint>

#include "IAICon.h"

#include "../../Obj/Obj_Char.h"
enum class E_AI_ConHP_OP
{
    Greater = 0, // Greater than
    Less = 1, // Less than
    Equal = 2, // Equal to
    GreaterEqual = 3, // Greater than or equal to
    LessEqual = 4, // Less than or equal to
    NotEqual = 5, // Not equal to
    None = 6, // None
    
};

class AIConHP:public IAICon
{
public:
    AIConHP(const Table_NpcAICondition * pCon):IAICon(pCon)
    {
		if (pCon)
		{
			m_nHP = pCon->GetParambyIndex(0);
			m_eOp = static_cast<E_AI_ConHP_OP>(pCon->GetParambyIndex(1));
		}
		else
		{
			m_nHP = 0;
			m_eOp = E_AI_ConHP_OP::None;
		}
    }
    ~AIConHP() = default;
public:  
    virtual bool IsSatisfy(Obj_Char* pOwner) override;
    int64_t m_nHP = 0; // Health points
    E_AI_ConHP_OP m_eOp = E_AI_ConHP_OP::None; // Operation type
    
};
