#pragma once
#include <cstdint>
#include "DbgInfo.h"

#define MAYBE_DEBUG \
    if(DbgIsManualEnable()) return true; \
    if(DbgIsManualDisable()) return false;


#define STATIC_INHERIT_DBG(this_point) \
    IDbgNess *dbgNess = static_cast<IDbgNess *>(this_point); 


class IDbgNess
{
public:
    IDbgNess();
    virtual ~IDbgNess() = default;
    int32_t         DbgGetId() const{return  m_nDbgId;}

    /*激活调试*/
    virtual DbgInfo FetchDbgInfo() const = 0;
    bool    DbgManualReset(){ m_bDbgManualDisable = false; m_bDbgManualEnable =false;}
    bool    DbgSetEnable() { m_bDbgManualEnable = true;}
    bool    DbgSetDisable() { m_bDbgManualDisable = true;}
    bool    DbgIsManualEnable() const{ return  m_bDbgManualEnable; }
    bool    DbgIsManualDisable() const {return  m_bDbgManualDisable;}

private:
    bool m_bDbgManualEnable = false; // 是否激活调试
    bool m_bDbgManualDisable = false; // 是否禁用调试
    int32_t m_nDbgId;
};
