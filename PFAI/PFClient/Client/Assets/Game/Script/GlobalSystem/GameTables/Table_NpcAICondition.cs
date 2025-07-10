//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAICondition : ITable 
{
 private const string TAB_NAME = "NpcAICondition";
 private int _row;
 private static TableSheet _gSheet_NpcAICondition = null;
 private Tab_NpcAICondition(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAICondition!=null) { _gSheet_NpcAICondition.Dispose(); _gSheet_NpcAICondition= null; }} 
 public static Tab_NpcAICondition NullData = new Tab_NpcAICondition(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAICondition == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAICondition(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAICondition other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAICondition == null) return;
 if (frameCount - _gSheet_NpcAICondition.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAICondition(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAICondition?.GetKey(_row)?? -1);} } 

public string Name { get {SafeCheck(); return _gSheet_NpcAICondition?.GetString(_row, 0)?? "";}} 

public int Type { get {SafeCheck(); return _gSheet_NpcAICondition?.GetInt(_row, 1)?? -1;}} 

public int getParamCount() { return 8; } 
 public int GetParambyIndex(int idx) {
 SafeCheck();
 if(idx>=0 && idx<8) return _gSheet_NpcAICondition?.GetInt(_row, 2+idx)?? -1; 
 return -1;
 }

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAICondition> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAICondition.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAICondition))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAICondition>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAICondition))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAICondition>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAICondition);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAICondition))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAICondition);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAICondition.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAICondition))
 {
 Debug.LogError($"LoadTable Error => NpcAICondition.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAICondition);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAICondition);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAICondition> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAICondition>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAICondition>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAICondition(i));
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

