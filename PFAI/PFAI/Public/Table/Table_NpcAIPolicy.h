/*Auto Created by Robot, Don't try to Modify*/
#pragma once

 #include "sol_table.h"

class Table_NpcAIPolicy
 {
 public:
 enum _ID
 {
 INVLAID_INDEX=-1,
ID_ID,
ID_GOALSENSORLIST=2,
ID_GOALSENSORPRORITY,
ID_BEHAVIORLIST,
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
 solar::table_string m_GoalSensorList;
 public:
 const char* GetGoalSensorList() const { return m_GoalSensorList.c_text(); }

private:
 solar::table_string m_GoalSensorPrority;
 public:
 const char* GetGoalSensorPrority() const { return m_GoalSensorPrority.c_text(); }

private:
 int32_t m_Id;
 public:
 int32_t GetId() const { return m_Id; }

};
 
 TABLE_ENTITY_DECL(Table_NpcAIPolicy);


