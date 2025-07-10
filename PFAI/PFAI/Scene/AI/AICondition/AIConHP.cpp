#include "AIConHP.h"
#include "Public.h"


    bool AIConHP::IsSatisfy(Obj_Char* pOwner)
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
        LOG_ERROR("AIConHP::IsSatisfy: Invalid operation type, type = {}", static_cast<int>(m_eOp));
		return false; // Default case, should not happen
    }
