#include "IBehavior.h"
#include "AIBSkill.h"
#include "AIBPatrol.h"
#include "Public.h"
#include "../Obj/Obj_Char.h"

class E_BehaviorType 
{
    public:
    enum {
        SKILL = 1,
        PATROL = 2,
    };
};
enum BehaviorType
{
    SKILL = 1,
    PATROL = 2,
};

//todo: 该类最后应该动态生成，而非硬编
class BehaviorFactory 
{
    public:
    static IBehavior * Create(Obj_Char* pOwner,int32_t behaviorCfgID) 
    {
        const Table_NpcAIBehavior * cfg = TABLE_GET_BY_ID(Table_NpcAIBehavior)(behaviorCfgID);
        if(cfg == nullptr) return nullptr;
        int type = cfg->GetType();
        switch (type) {
            case E_BehaviorType::SKILL: return new AIBSkill(pOwner, cfg);
            case E_BehaviorType::PATROL: return new AIBPatrol(pOwner, cfg);
            default: return nullptr;
        }
    }
};