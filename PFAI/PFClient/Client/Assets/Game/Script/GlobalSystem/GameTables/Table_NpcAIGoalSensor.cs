//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAIGoalSensor : ITable 
{
 private const string TAB_NAME = "NpcAIGoalSensor";
 private int _row;
 private static TableSheet _gSheet_NpcAIGoalSensor = null;
 private Tab_NpcAIGoalSensor(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAIGoalSensor!=null) { _gSheet_NpcAIGoalSensor.Dispose(); _gSheet_NpcAIGoalSensor= null; }} 
 public static Tab_NpcAIGoalSensor NullData = new Tab_NpcAIGoalSensor(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAIGoalSensor == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAIGoalSensor(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAIGoalSensor other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAIGoalSensor == null) return;
 if (frameCount - _gSheet_NpcAIGoalSensor.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAIGoalSensor(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAIGoalSensor?.GetKey(_row)?? -1);} } 

public string Name { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetString(_row, 0)?? "";}} 

public int Type { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetInt(_row, 1)?? -1;}} 

public string ConditionList { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetString(_row, 2)?? "";}} 

public string BehaviorList { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetString(_row, 3)?? "";}} 

public int Prority { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetInt(_row, 4)?? -1;}} 

public int CalGoalInterval { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetInt(_row, 5)?? -1;}} 

public int GoalTimeOut { get {SafeCheck(); return _gSheet_NpcAIGoalSensor?.GetInt(_row, 6)?? -1;}} 

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAIGoalSensor> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAIGoalSensor.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAIGoalSensor))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIGoalSensor>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIGoalSensor))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIGoalSensor>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIGoalSensor);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAIGoalSensor))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAIGoalSensor);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAIGoalSensor.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIGoalSensor))
 {
 Debug.LogError($"LoadTable Error => NpcAIGoalSensor.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIGoalSensor);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAIGoalSensor);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAIGoalSensor> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIGoalSensor>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIGoalSensor>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAIGoalSensor(i));
 }
 }
 
 public override int GetHashCode()
 {
 return _row;
 }
 
 public void SetRow(int index)
 {
 _row = index;
 }


}
}

