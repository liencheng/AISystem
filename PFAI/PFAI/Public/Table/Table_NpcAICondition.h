/*Auto Created by Robot, Don't try to Modify*/
#pragma once

 #include "sol_table.h"
#include <cstdint>

class Table_NpcAICondition
 {
 public:
 enum _ID
 {
 INVLAID_INDEX=-1,
ID_ID,
ID_NAME=2,
ID_TYPE,
ID_PARAM_0,
ID_PARAM_1,
ID_PARAM_2,
ID_PARAM_3,
ID_PARAM_4,
ID_PARAM_5,
ID_PARAM_6,
ID_PARAM_7,
ID_TAB_CURCOL_COUNT,
TABLE_MAX_ID=1000,
TABLE_MAX_RECORD=1000
 };
 
 public:
 bool load(const solar::table_file &rDB, int32_t nRow);
 
 public:
 static const char * file_path(void);

private:
 int32_t m_Id;
 public:
 int32_t GetId() const { return m_Id; }

private:
 solar::table_string m_Name;
 public:
 const char* GetName() const { return m_Name.c_text(); }

public:
 int32_t getParamCount() const { return 8; } 
 private:
 int32_t m_Param[8];
 public:
 int32_t GetParambyIndex(int32_t idx) const 
 {
 if(idx>=0 && idx<8) return m_Param[idx];
 return -1;
 }

private:
 int32_t m_Type;
 public:
 int32_t GetType() const { return m_Type; }

};
 
 TABLE_ENTITY_DECL(Table_NpcAICondition);


