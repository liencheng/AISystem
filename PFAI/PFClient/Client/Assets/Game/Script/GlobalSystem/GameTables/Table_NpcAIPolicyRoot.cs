//Auto Created by Robot, Don't try to Modify
using System;
 using Unity.Collections;
 using Unity.Collections.LowLevel.Unsafe;
 using UnityEngine;
 using System.IO;

namespace Games.Table{
public struct Tab_NpcAIPolicyRoot : ITable 
{
 private const string TAB_NAME = "NpcAIPolicyRoot";
 private int _row;
 private static TableSheet _gSheet_NpcAIPolicyRoot = null;
 private Tab_NpcAIPolicyRoot(int row)
 {
 _row = row;
 }
 public static void Clean() {if(_gSheet_NpcAIPolicyRoot!=null) { _gSheet_NpcAIPolicyRoot.Dispose(); _gSheet_NpcAIPolicyRoot= null; }} 
 public static Tab_NpcAIPolicyRoot NullData = new Tab_NpcAIPolicyRoot(TableManager.NullRowIndex);
 private void SafeCheck() { if (_gSheet_NpcAIPolicyRoot == null && _row != TableManager.NullRowIndex) { Debug.LogWarning($"Do not Hold On Table {TAB_NAME} Var"); TableManager.InitTable_NpcAIPolicyRoot(true,false);}} 
 public bool IsNull() => _row == TableManager.NullRowIndex; 
 public bool IsNotNull() => _row != TableManager.NullRowIndex; 
 public bool IsEqual(Tab_NpcAIPolicyRoot other) => _row == other._row; 
 public static void AutoRelease(int frameCount){
 if (_gSheet_NpcAIPolicyRoot == null) return;
 if (frameCount - _gSheet_NpcAIPolicyRoot.AccessTime > TableManager.AutoReleaseTimeCount){
 Games.Table.TableManager.InitTable_NpcAIPolicyRoot(false,false);
 }
 }

public int Id { get {SafeCheck(); return (int)(_gSheet_NpcAIPolicyRoot?.GetKey(_row)?? -1);} } 

public int PolicyId { get {SafeCheck(); return _gSheet_NpcAIPolicyRoot?.GetInt(_row, 0)?? -1;}} 

public static void LoadTable(ref NativeHashMap<int, Tab_NpcAIPolicyRoot> table, bool bCreate = false, byte[] bytes = null)
 {
 #if USE_TABLE_AB || !UNITY_EDITOR
 TextAsset asset = AssetManager.LoadTableAssetSync($"Tab_{TAB_NAME}_Data","NpcAIPolicyRoot.txt",out var isByteAsset);
 if(isByteAsset)
 {
 if(asset == null || !TableSheet.LoadBinarySheet(asset.bytes,out _gSheet_NpcAIPolicyRoot))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.bytes == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated){ table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIPolicyRoot>(0, Allocator.Persistent,true);
 return;
 }
 }
 else
 {
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIPolicyRoot))
 {
 Debug.LogError($"LoadTable Error => {TAB_NAME} {(asset == null || asset.text == null ? "asset is Null " : "DeSerializeTable Failed")}");
 asset = null;
 if(table.IsCreated) { table.Dispose();}
 table = new NativeHashMap<int, Tab_NpcAIPolicyRoot>(0, Allocator.Persistent,true);
 return;
 }
 }
 if (asset != null)
 {
 //Resources.UnloadAsset(asset);
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicyRoot);
 asset = null;
 #else
 if (bytes != null && TableSheet.LoadBinarySheet(bytes, out _gSheet_NpcAIPolicyRoot))
 {
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicyRoot);
 return;
 }
 TextAsset asset = UnityEditor.AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Game/Table/NpcAIPolicyRoot.txt");
 if(asset == null || !TableSheet.LoadTextSheet(asset.text,out _gSheet_NpcAIPolicyRoot))
 {
 Debug.LogError($"LoadTable Error => NpcAIPolicyRoot.txt {(asset == null || asset.text == null ? "asset is Null" : "DeSerializeTable Failed")} ");
 asset = null;
 return;
 }
 LoadTableBySheet(ref table, ref _gSheet_NpcAIPolicyRoot);
 asset = null;
 #endif
 if (bCreate)
 {
 TableHelper.SerializeTable(TAB_NAME,ref _gSheet_NpcAIPolicyRoot);
 }
 }
 private static void LoadTableBySheet(ref NativeHashMap<int, Tab_NpcAIPolicyRoot> table, ref TableSheet sheet)
 {
 NativeArray<int>keyArray = sheet.KeyArrayNative; 
 if(!keyArray.IsCreated || keyArray.Length == 0)
 {
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIPolicyRoot>(0, Allocator.Persistent,true);
 return;
 };
 if(table.IsCreated) { table.Dispose(); }
 table = new NativeHashMap<int, Tab_NpcAIPolicyRoot>(keyArray.Length, Allocator.Persistent,true);
 for (var i = 0; i < keyArray.Length; i++)
 {
 table.Add(keyArray[i],new Tab_NpcAIPolicyRoot(i));
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

