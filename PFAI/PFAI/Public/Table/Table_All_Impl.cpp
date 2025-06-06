/*Auto Created by Robot, Don't try to Modify*/
#include "Public.h"
 #if defined(_GAMESERVER_)
 #include "Table_NpcAIBehavior.h"






bool Table_NpcAIBehavior::load(const solar::table_file &rDB, int32_t nRow)
 {
 __SOL_TRACE
 
 SOL_ASSERT(ID_TAB_CURCOL_COUNT==rDB.get_filed_count(), "NpcAIBehavior Columns Differ"); 
 rDB.read(m_CD,nRow,(int32_t)ID_CD);
rDB.read(m_ConditionList,nRow,(int32_t)ID_CONDITIONLIST);
rDB.read(m_Id,nRow,(int32_t)ID_ID);
rDB.read(m_Param[0],nRow,(int32_t)ID_PARAM_0);
rDB.read(m_Param[1],nRow,(int32_t)ID_PARAM_1);
rDB.read(m_Param[2],nRow,(int32_t)ID_PARAM_2);
rDB.read(m_Param[3],nRow,(int32_t)ID_PARAM_3);
rDB.read(m_Param[4],nRow,(int32_t)ID_PARAM_4);
rDB.read(m_Param[5],nRow,(int32_t)ID_PARAM_5);
rDB.read(m_Param[6],nRow,(int32_t)ID_PARAM_6);
rDB.read(m_Param[7],nRow,(int32_t)ID_PARAM_7);
rDB.read(m_Type,nRow,(int32_t)ID_TYPE);

 return true;
 SOL_TRACE__
 return false;
 }
 
 const char * Table_NpcAIBehavior::file_path(void)
 {
 return "Config/NpcAIBehavior.txt";
 }


 TABLE_ENTITY_IMPL(Table_NpcAIBehavior);

#endif 
 

/*Auto Created by Robot, Don't try to Modify*/
#include "Public.h"
 #if defined(_GAMESERVER_)
 #include "Table_NpcAICondition.h"





bool Table_NpcAICondition::load(const solar::table_file &rDB, int32_t nRow)
 {
 __SOL_TRACE
 
 SOL_ASSERT(ID_TAB_CURCOL_COUNT==rDB.get_filed_count(), "NpcAICondition Columns Differ"); 
 rDB.read(m_Id,nRow,(int32_t)ID_ID);
rDB.read(m_Name,nRow,(int32_t)ID_NAME);
rDB.read(m_Param[0],nRow,(int32_t)ID_PARAM_0);
rDB.read(m_Param[1],nRow,(int32_t)ID_PARAM_1);
rDB.read(m_Param[2],nRow,(int32_t)ID_PARAM_2);
rDB.read(m_Param[3],nRow,(int32_t)ID_PARAM_3);
rDB.read(m_Param[4],nRow,(int32_t)ID_PARAM_4);
rDB.read(m_Param[5],nRow,(int32_t)ID_PARAM_5);
rDB.read(m_Param[6],nRow,(int32_t)ID_PARAM_6);
rDB.read(m_Param[7],nRow,(int32_t)ID_PARAM_7);
rDB.read(m_Type,nRow,(int32_t)ID_TYPE);

 return true;
 SOL_TRACE__
 return false;
 }
 
 const char * Table_NpcAICondition::file_path(void)
 {
 return "Config/NpcAICondition.txt";
 }


 TABLE_ENTITY_IMPL(Table_NpcAICondition);

#endif 
 

/*Auto Created by Robot, Don't try to Modify*/
#include "Public.h"
 #if defined(_GAMESERVER_)
 #include "Table_NpcAIGoalSensor.h"






bool Table_NpcAIGoalSensor::load(const solar::table_file &rDB, int32_t nRow)
 {
 __SOL_TRACE
 
 SOL_ASSERT(ID_TAB_CURCOL_COUNT==rDB.get_filed_count(), "NpcAIGoalSensor Columns Differ"); 
 rDB.read(m_ConditionList,nRow,(int32_t)ID_CONDITIONLIST);
rDB.read(m_Id,nRow,(int32_t)ID_ID);
rDB.read(m_Name,nRow,(int32_t)ID_NAME);
rDB.read(m_Prority,nRow,(int32_t)ID_PRORITY);
rDB.read(m_Type,nRow,(int32_t)ID_TYPE);

 return true;
 SOL_TRACE__
 return false;
 }
 
 const char * Table_NpcAIGoalSensor::file_path(void)
 {
 return "Config/NpcAIGoalSensor.txt";
 }


 TABLE_ENTITY_IMPL(Table_NpcAIGoalSensor);

#endif 
 

/*Auto Created by Robot, Don't try to Modify*/
#include "Public.h"
 #if defined(_GAMESERVER_)
 #include "Table_NpcAIPolicy.h"





bool Table_NpcAIPolicy::load(const solar::table_file &rDB, int32_t nRow)
 {
 __SOL_TRACE
 
 SOL_ASSERT(ID_TAB_CURCOL_COUNT==rDB.get_filed_count(), "NpcAIPolicy Columns Differ"); 
 rDB.read(m_BehaviorList,nRow,(int32_t)ID_BEHAVIORLIST);
rDB.read(m_GoalSensorList,nRow,(int32_t)ID_GOALSENSORLIST);
rDB.read(m_GoalSensorPrority,nRow,(int32_t)ID_GOALSENSORPRORITY);
rDB.read(m_Id,nRow,(int32_t)ID_ID);

 return true;
 SOL_TRACE__
 return false;
 }
 
 const char * Table_NpcAIPolicy::file_path(void)
 {
 return "Config/NpcAIPolicy.txt";
 }


 TABLE_ENTITY_IMPL(Table_NpcAIPolicy);

#endif 
 

/*Auto Created by Robot, Don't try to Modify*/
#include "Public.h"
 #if defined(_GAMESERVER_)
 #include "Table_NpcAIPolicyRoot.h"



bool Table_NpcAIPolicyRoot::load(const solar::table_file &rDB, int32_t nRow)
 {
 __SOL_TRACE
 
 SOL_ASSERT(ID_TAB_CURCOL_COUNT==rDB.get_filed_count(), "NpcAIPolicyRoot Columns Differ"); 
 rDB.read(m_Id,nRow,(int32_t)ID_ID);
rDB.read(m_PolicyId,nRow,(int32_t)ID_POLICYID);

 return true;
 SOL_TRACE__
 return false;
 }
 
 const char * Table_NpcAIPolicyRoot::file_path(void)
 {
 return "Config/NpcAIPolicyRoot.txt";
 }


 TABLE_ENTITY_IMPL(Table_NpcAIPolicyRoot);

#endif 
 

