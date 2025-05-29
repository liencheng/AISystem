#include "IDbgNess.h"


int32_t g_dbg_serial_id = 0;
int32_t GenDbgId()
{
   return g_dbg_serial_id++; 
}

IDbgNess::IDbgNess()
{
   m_nDbgId = GenDbgId(); 
}


