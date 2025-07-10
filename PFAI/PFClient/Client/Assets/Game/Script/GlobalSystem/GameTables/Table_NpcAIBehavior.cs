//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAIBehavior : ITable 
{
 private const string TAB_NAME = "NpcAIBehavior";
 private int _row;
 private static TableSheet _gSheet_NpcAIBehavior = null;
 private Tab_NpcAIBehavior(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAIBehavior!=null) { _gSheet_NpcAIBehavior.Dispose(); _gSheet_NpcAIBehavior= null; }} 
 public static Tab_NpcAIBehavior NullData = new Tab_NpcAIBehavior(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAIBehavior == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAIBehavior(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAIBehavior other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAIBehavior == null) return;
 if (frameCount - _gSheet_NpcAIBehavior.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAIBehavior(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAIBehavior?.GetKey(_row)?? -1);} } 

public float CD { get {SafeCheck(); return _gSheet_NpcAIBehavior?.GetFloat(_row, 0)?? 0.0f;}} 

public int Timeout { get {SafeCheck(); return _gSheet_NpcAIBehavior?.GetInt(_row, 1)?? -1;}} 

public string ConditionList { get {SafeCheck(); return _gSheet_NpcAIBehavior?.GetString(_row, 2)?? "";}} 

public int Proprity { get {SafeCheck(); return _gSheet_NpcAIBehavior?.GetInt(_row, 3)?? -1;}} 

public int Type { get {SafeCheck(); return _gSheet_NpcAIBehavior?.GetInt(_row, 4)?? -1;}} 

public int getParamCount() { return 8; } 
 public int GetParambyIndex(int idx) {
 SafeCheck();
 if(idx>=0 && idx<8) return _gSheet_NpcAIBehavior?.GetInt(_row, 5+idx)?? -1; 
 return -1;
 }

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAIBehavior> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAIBehavior.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAIBehavior))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIBehavior>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIBehavior))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIBehavior>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIBehavior);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAIBehavior))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAIBehavior);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAIBehavior.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIBehavior))
 {
 Debug.LogError($"LoadTable Error => NpcAIBehavior.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIBehavior);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAIBehavior);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAIBehavior> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIBehavior>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIBehavior>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAIBehavior(i));
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

