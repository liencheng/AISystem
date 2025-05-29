#pragma once
#include <cstdint>

#include "../AIDebugable/IDbgNess.h"

class Obj_Char;

class IAICon: public IDbgNess
{
public:
    IAICon(int32_t id) : m_CfgId(id) {} // Constructor to initialize the condition ID
    virtual ~IAICon() = default; // Virtual destructor for proper cleanup
    
    int32_t GetId() const { return m_CfgId; } // Get the ID of the condition
    virtual bool IsSatisfy(Obj_Char * pOwner) {MAYBE_DEBUG;}

protected:
    int32_t     m_CfgId = 0; // ID of the condition,link to AIConditionCfg.txt
    
};
