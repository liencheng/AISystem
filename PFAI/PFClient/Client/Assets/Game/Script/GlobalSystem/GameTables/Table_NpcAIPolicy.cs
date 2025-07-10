//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAIPolicy : ITable 
{
 private const string TAB_NAME = "NpcAIPolicy";
 private int _row;
 private static TableSheet _gSheet_NpcAIPolicy = null;
 private Tab_NpcAIPolicy(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAIPolicy!=null) { _gSheet_NpcAIPolicy.Dispose(); _gSheet_NpcAIPolicy= null; }} 
 public static Tab_NpcAIPolicy NullData = new Tab_NpcAIPolicy(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAIPolicy == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAIPolicy(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAIPolicy other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAIPolicy == null) return;
 if (frameCount - _gSheet_NpcAIPolicy.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAIPolicy(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAIPolicy?.GetKey(_row)?? -1);} } 

public string GoalSensorList { get {SafeCheck(); return _gSheet_NpcAIPolicy?.GetString(_row, 0)?? "";}} 

public string GoalSensorPrority { get {SafeCheck(); return _gSheet_NpcAIPolicy?.GetString(_row, 1)?? "";}} 

public string BehaviorList { get {SafeCheck(); return _gSheet_NpcAIPolicy?.GetString(_row, 2)?? "";}} 

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAIPolicy> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAIPolicy.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAIPolicy))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIPolicy>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIPolicy))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIPolicy>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicy);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAIPolicy))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicy);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAIPolicy.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIPolicy))
 {
 Debug.LogError($"LoadTable Error => NpcAIPolicy.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicy);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAIPolicy);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAIPolicy> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIPolicy>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIPolicy>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAIPolicy(i));
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

