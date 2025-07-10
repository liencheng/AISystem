/*Auto Created by Robot, Don't try to Modify*/
#pragma once

 #include "sol_table.h"

class Table_NpcAISignal
 {
 public:
 enum _ID
 {
 INVLAID_INDEX=-1,
ID_ID,
ID_NAME=2,
ID_TYPE,
ID_CONDITIONLIST,
ID_BEHAVIORLIST,
ID_PRORITY,
ID_TAB_CURCOL_COUNT,
TABLE_MAX_ID=1000,
TABLE_MAX_RECORD=1000
 };
 
 public:
 bool load(const solar::table_file &rDB, int32_t nRow);
 
 public:
 static const char * file_path(void);

private:
 solar::table_string m_BehaviorList;
 public:
 const char* GetBehaviorList() const { return m_BehaviorList.c_text(); }

private:
 solar::table_string m_ConditionList;
 public:
 const char* GetConditionList() const { return m_ConditionList.c_text(); }

private:
 int32_t m_Id;
 public:
 int32_t GetId() const { return m_Id; }

private:
 solar::table_string m_Name;
 public:
 const char* GetName() const { return m_Name.c_text(); }

private:
 int32_t m_Prority;
 public:
 int32_t GetPrority() const { return m_Prority; }

private:
 int32_t m_Type;
 public:
 int32_t GetType() const { return m_Type; }

};
 
 TABLE_ENTITY_DECL(Table_NpcAISignal);


