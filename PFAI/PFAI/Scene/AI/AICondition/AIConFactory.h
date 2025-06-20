#include "Public.h"
#include "IAICon.h"
#include "AIConMP.h"
#include "AIConHP.h"
#include "AIConInCombat.h"
#include "AIConGoToPoint.h"


class AIConFactory
{

public:
	static IAICon* CreateAICondition(const Table_NpcAICondition* pConCfg)
	{
		int32_t nConType = pConCfg->GetType();
		switch (nConType)
		{
		case E_AIConType::E_CON_HP:
			return new AIConHP(pConCfg);
			break;
		case E_AIConType::E_CON_MP:
			return new AIConMP(pConCfg);
			break;
		case E_AIConType::E_CON_COMBAT:
			return new AIConInCombat(pConCfg);
			break;
		default:
			LOG_ERROR("Unknown AI Condition: " + std::to_string(nConType));
			return nullptr;
			break;
		}
	}
};
