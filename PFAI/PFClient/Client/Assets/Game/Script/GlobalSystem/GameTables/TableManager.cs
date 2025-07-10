//Auto Created by Robot, Don't try to Modify
using System;
 using System.Collections.Generic;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public partial class TableManager {
 public const int NullRowIndex = int.MinValue;
 public const int AutoReleaseTimeCount = 18000;
 public static bool m_LoadClientBlockData = false;

private static NativeHashMap<int, Tab_NpcAIBehavior> g_NpcAIBehavior ;
 
 public static void InitTable_NpcAIBehavior(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAIBehavior.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAIBehavior.IsCreated)
 {
 g_NpcAIBehavior.Dispose();
 }
 Tab_NpcAIBehavior.Clean();
 return ;
 }
 Tab_NpcAIBehavior.LoadTable(ref g_NpcAIBehavior,createDatFile,bytes);
 }
private static NativeHashMap<int, Tab_NpcAICondition> g_NpcAICondition ;
 
 public static void InitTable_NpcAICondition(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAICondition.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAICondition.IsCreated)
 {
 g_NpcAICondition.Dispose();
 }
 Tab_NpcAICondition.Clean();
 return ;
 }
 Tab_NpcAICondition.LoadTable(ref g_NpcAICondition,createDatFile,bytes);
 }
private static NativeHashMap<int, Tab_NpcAIGoalSensor> g_NpcAIGoalSensor ;
 
 public static void InitTable_NpcAIGoalSensor(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAIGoalSensor.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAIGoalSensor.IsCreated)
 {
 g_NpcAIGoalSensor.Dispose();
 }
 Tab_NpcAIGoalSensor.Clean();
 return ;
 }
 Tab_NpcAIGoalSensor.LoadTable(ref g_NpcAIGoalSensor,createDatFile,bytes);
 }
private static NativeHashMap<int, Tab_NpcAIPolicy> g_NpcAIPolicy ;
 
 public static void InitTable_NpcAIPolicy(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAIPolicy.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAIPolicy.IsCreated)
 {
 g_NpcAIPolicy.Dispose();
 }
 Tab_NpcAIPolicy.Clean();
 return ;
 }
 Tab_NpcAIPolicy.LoadTable(ref g_NpcAIPolicy,createDatFile,bytes);
 }
private static NativeHashMap<int, Tab_NpcAIPolicyRoot> g_NpcAIPolicyRoot ;
 
 public static void InitTable_NpcAIPolicyRoot(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAIPolicyRoot.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAIPolicyRoot.IsCreated)
 {
 g_NpcAIPolicyRoot.Dispose();
 }
 Tab_NpcAIPolicyRoot.Clean();
 return ;
 }
 Tab_NpcAIPolicyRoot.LoadTable(ref g_NpcAIPolicyRoot,createDatFile,bytes);
 }
private static NativeHashMap<int, Tab_NpcAISignal> g_NpcAISignal ;
 
 public static void InitTable_NpcAISignal(bool bLoadTable = true, bool createDatFile = false, byte[] bytes = null, int autoRelaseFrameCount=-1)
 {
 if(autoRelaseFrameCount > 0){
 Tab_NpcAISignal.AutoRelease(autoRelaseFrameCount);
 return;
 }
 if(bLoadTable == false)
 {
 if(g_NpcAISignal.IsCreated)
 {
 g_NpcAISignal.Dispose();
 }
 Tab_NpcAISignal.Clean();
 return ;
 }
 Tab_NpcAISignal.LoadTable(ref g_NpcAISignal,createDatFile,bytes);
 }
public static void InitTable(bool bLoadTable = true, bool createDatFile = false, int autoReleaseFrameCount=-1)
 {
 if(autoReleaseFrameCount == -1){
 }
 InitTable_NpcAIBehavior(bLoadTable,createDatFile,null,autoReleaseFrameCount);

InitTable_NpcAICondition(bLoadTable,createDatFile,null,autoReleaseFrameCount);

InitTable_NpcAIGoalSensor(bLoadTable,createDatFile,null,autoReleaseFrameCount);

InitTable_NpcAIPolicy(bLoadTable,createDatFile,null,autoReleaseFrameCount);

InitTable_NpcAIPolicyRoot(bLoadTable,createDatFile,null,autoReleaseFrameCount);

InitTable_NpcAISignal(bLoadTable,createDatFile,null,autoReleaseFrameCount);


 #if UNITY_EDITOR
 if (createDatFile)
 {
 UnityEditor.AssetDatabase.SaveAssets();
 }
 #endif
 }

public static Tab_NpcAIBehavior GetNpcAIBehaviorByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAIBehavior.IsCreated)
 {
 InitTable_NpcAIBehavior();
 }
 if( g_NpcAIBehavior.ContainsKey(nKey))
 {
 return g_NpcAIBehavior[nKey];
 }
 return Tab_NpcAIBehavior.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAIBehavior> GetNpcAIBehavior()
 {
 if(!g_NpcAIBehavior.IsCreated)
 {
 InitTable_NpcAIBehavior();
 }
 return g_NpcAIBehavior;
 }

public static Tab_NpcAICondition GetNpcAIConditionByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAICondition.IsCreated)
 {
 InitTable_NpcAICondition();
 }
 if( g_NpcAICondition.ContainsKey(nKey))
 {
 return g_NpcAICondition[nKey];
 }
 return Tab_NpcAICondition.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAICondition> GetNpcAICondition()
 {
 if(!g_NpcAICondition.IsCreated)
 {
 InitTable_NpcAICondition();
 }
 return g_NpcAICondition;
 }

public static Tab_NpcAIGoalSensor GetNpcAIGoalSensorByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAIGoalSensor.IsCreated)
 {
 InitTable_NpcAIGoalSensor();
 }
 if( g_NpcAIGoalSensor.ContainsKey(nKey))
 {
 return g_NpcAIGoalSensor[nKey];
 }
 return Tab_NpcAIGoalSensor.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAIGoalSensor> GetNpcAIGoalSensor()
 {
 if(!g_NpcAIGoalSensor.IsCreated)
 {
 InitTable_NpcAIGoalSensor();
 }
 return g_NpcAIGoalSensor;
 }

public static Tab_NpcAIPolicy GetNpcAIPolicyByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAIPolicy.IsCreated)
 {
 InitTable_NpcAIPolicy();
 }
 if( g_NpcAIPolicy.ContainsKey(nKey))
 {
 return g_NpcAIPolicy[nKey];
 }
 return Tab_NpcAIPolicy.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAIPolicy> GetNpcAIPolicy()
 {
 if(!g_NpcAIPolicy.IsCreated)
 {
 InitTable_NpcAIPolicy();
 }
 return g_NpcAIPolicy;
 }

public static Tab_NpcAIPolicyRoot GetNpcAIPolicyRootByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAIPolicyRoot.IsCreated)
 {
 InitTable_NpcAIPolicyRoot();
 }
 if( g_NpcAIPolicyRoot.ContainsKey(nKey))
 {
 return g_NpcAIPolicyRoot[nKey];
 }
 return Tab_NpcAIPolicyRoot.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAIPolicyRoot> GetNpcAIPolicyRoot()
 {
 if(!g_NpcAIPolicyRoot.IsCreated)
 {
 InitTable_NpcAIPolicyRoot();
 }
 return g_NpcAIPolicyRoot;
 }

public static Tab_NpcAISignal GetNpcAISignalByID(int nKey, int nIndex = 0)
 {
 if(!g_NpcAISignal.IsCreated)
 {
 InitTable_NpcAISignal();
 }
 if( g_NpcAISignal.ContainsKey(nKey))
 {
 return g_NpcAISignal[nKey];
 }
 return Tab_NpcAISignal.NullData;
 }
 public static NativeHashMap<int, Tab_NpcAISignal> GetNpcAISignal()
 {
 if(!g_NpcAISignal.IsCreated)
 {
 InitTable_NpcAISignal();
 }
 return g_NpcAISignal;
 }


}
}

