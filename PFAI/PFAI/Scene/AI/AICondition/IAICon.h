#pragma once
#include <cstdint>
#include "Public.h"
#include "../AIDebugable/IDbgNess.h"

class Obj_Char;

class E_AIConType
{
public:
    enum
    {
		E_CON_None = 0, // 无条件
		E_CON_HP, // 健康条件
		E_CON_MP,
		E_CON_COMBAT, // 战斗状态条件
		E_CON_Distance,
    };
};

class IAICon: public IDbgNess
{
public:
    IAICon(const Table_NpcAICondition * pCon){
        if (pCon)
        {
			m_CfgId = pCon->GetId(); // Initialize the condition ID from the configuration
        }
    } // Constructor to initialize the condition ID
    virtual ~IAICon() = default; // Virtual destructor for proper cleanup
	virtual DbgInfo FetchDbgInfo() const override
	{
	}
    
    int32_t GetId() const { return m_CfgId; } // Get the ID of the condition
    virtual bool IsSatisfy(Obj_Char * pOwner) {MAYBE_DEBUG; return false; } // Check if the condition is satisfied


protected:
    int32_t     m_CfgId = 0; // ID of the condition,link to AIConditionCfg.txt
    
};
