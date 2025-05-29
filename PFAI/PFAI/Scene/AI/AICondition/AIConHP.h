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

class AIConHP:IAICon
{
public:
    AIConHP(int64_t nHP, E_AI_ConHP_OP eOp)
        :m_nHP(nHP), m_eOp(eOp)
    {
        
    }
    ~AIConHP() = default;
public:  
    virtual bool IsSatisfy(Obj_Char* pOwner) override
    {
        MAYBE_DEBUG;
        
        switch (m_eOp)
        {
            case E_AI_ConHP_OP::Greater:
                return pOwner->GetHP() > m_nHP;
            case E_AI_ConHP_OP::Less:
                return pOwner->GetHP() < m_nHP;
            case E_AI_ConHP_OP::Equal:
                return pOwner->GetHP() == m_nHP;
            case E_AI_ConHP_OP::GreaterEqual:
                return pOwner->GetHP() >= m_nHP;
            case E_AI_ConHP_OP::LessEqual:
                return pOwner->GetHP() <= m_nHP;
            case E_AI_ConHP_OP::NotEqual:
                return pOwner->GetHP() != m_nHP;
            case E_AI_ConHP_OP::None:
                return false;
        }
    }
private:
    int64_t m_nHP = 0; // Health points
    E_AI_ConHP_OP m_eOp = E_AI_ConHP_OP::None; // Operation type
    
};
