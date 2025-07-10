//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAISignal : ITable 
{
 private const string TAB_NAME = "NpcAISignal";
 private int _row;
 private static TableSheet _gSheet_NpcAISignal = null;
 private Tab_NpcAISignal(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAISignal!=null) { _gSheet_NpcAISignal.Dispose(); _gSheet_NpcAISignal= null; }} 
 public static Tab_NpcAISignal NullData = new Tab_NpcAISignal(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAISignal == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAISignal(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAISignal other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAISignal == null) return;
 if (frameCount - _gSheet_NpcAISignal.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAISignal(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAISignal?.GetKey(_row)?? -1);} } 

public string Name { get {SafeCheck(); return _gSheet_NpcAISignal?.GetString(_row, 0)?? "";}} 

public int Type { get {SafeCheck(); return _gSheet_NpcAISignal?.GetInt(_row, 1)?? -1;}} 

public string ConditionList { get {SafeCheck(); return _gSheet_NpcAISignal?.GetString(_row, 2)?? "";}} 

public string BehaviorList { get {SafeCheck(); return _gSheet_NpcAISignal?.GetString(_row, 3)?? "";}} 

public int Prority { get {SafeCheck(); return _gSheet_NpcAISignal?.GetInt(_row, 4)?? -1;}} 

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAISignal> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAISignal.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAISignal))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAISignal>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAISignal))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAISignal>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAISignal);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAISignal))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAISignal);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAISignal.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAISignal))
 {
 Debug.LogError($"LoadTable Error => NpcAISignal.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAISignal);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAISignal);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAISignal> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAISignal>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAISignal>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAISignal(i));
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

