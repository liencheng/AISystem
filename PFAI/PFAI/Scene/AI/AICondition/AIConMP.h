#pragma once
#include <cstdint>
#include "IAICon.h"
#include "../../Obj/Obj_Char.h"

enum class E_AI_ConMP_OP
{
    Greater = 0, // Greater than
    Less = 1, // Less than
    Equal = 2, // Equal to
    GreaterEqual = 3, // Greater than or equal to
    LessEqual = 4, // Less than or equal to
    NotEqual = 5, // Not equal to
    None = 6, // None
};

class AIConMP:IAICon
{
public:
    AIConMP(int64_t nMP, E_AI_ConMP_OP eOp)
        :m_nMP(nMP), m_eOp(eOp)
    {
        
    }
    ~AIConMP() = default;
    
    virtual bool IsSatisfy(Obj_Char* pOwner) override
    {
        switch (m_eOp)
        {
        case E_AI_ConMP_OP::Greater:
            return pOwner->GetMP() > m_nMP;
        case E_AI_ConMP_OP::Less:
            return pOwner->GetMP() < m_nMP;
        case E_AI_ConMP_OP::Equal:
            return pOwner->GetMP() == m_nMP;
        case E_AI_ConMP_OP::GreaterEqual:
            return pOwner->GetMP() >= m_nMP;
        case E_AI_ConMP_OP::LessEqual:
            return pOwner->GetMP() <= m_nMP;
        case E_AI_ConMP_OP::NotEqual:
            return pOwner->GetMP() != m_nMP;
        case E_AI_ConMP_OP::None:
            return false;
        }
    }
private:
    int64_t m_nMP = 0; // Magic points
    E_AI_ConMP_OP m_eOp = E_AI_ConMP_OP::None; // Operation type
};