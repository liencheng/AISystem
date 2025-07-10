/*Auto Created by Robot, Don't try to Modify*/
#pragma once

 #include "sol_table.h"

class Table_NpcAIPolicyRoot
 {
 public:
 enum _ID
 {
 INVLAID_INDEX=-1,
ID_ID,
ID_POLICYID=2,
ID_TAB_CURCOL_COUNT,
TABLE_MAX_ID=60000,
TABLE_MAX_RECORD=60000
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
 int32_t m_PolicyId;
 public:
 int32_t GetPolicyId() const { return m_PolicyId; }

};
 
 TABLE_ENTITY_DECL(Table_NpcAIPolicyRoot);


