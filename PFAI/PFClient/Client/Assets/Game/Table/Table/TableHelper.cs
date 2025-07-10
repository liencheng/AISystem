// Description: 读取表格数据的帮助类

using System;
using System.Collections.Generic;
using Unity.Collections;
using UnityEngine;

namespace Games.Table
{ 
public interface ITable
{
    public void SetRow(int index); 
} 

public static class TableHelper
{ 
    public static bool DeSerializeTable<T>(byte[] bytes,ref Dictionary<int,T> table,ref TableSheet sheet) where T : ITable , new()
    {
        try
        {
            if (!TableSheet.LoadBinarySheet(bytes, out sheet))
            {
                Debug.LogError("DeSerializeTable Error => LoadBinarySheet");
                return false;
            }
            _LoadTable(ref sheet,ref table);  
        }
        catch (System.Exception e)
        { 
            Debug.LogError($"DeSerializeTable Byte => {e.Message}"); 
            return false;
        } 
        return true;
    }
    
    public static bool DeSerializeTable<T>(string text,ref Dictionary<int,T> table, ref TableSheet sheet) where T : ITable , new()
    {    
        try
        {
            if (!TableSheet.LoadTextSheet(text, out sheet))
            { 
                Debug.LogError("DeSerializeTable Error => LoadTextSheet");
                return false;
            }
            _LoadTable(ref sheet,ref table);  
        }
        catch (System.Exception e)
        { 
            Debug.LogError($"DeSerializeTable Text => {e.Message}"); 
            return false;
        } 
        return true;
    }  
    
    public static void SerializeTable(string tableName,ref TableSheet sheet)  
    {   
        sheet.SaveBinarySheet(tableName);
    } 
  
    
    private static void _LoadTable<T>(ref TableSheet tableSheet, ref Dictionary<int, T> table) where T : ITable, new()
    { 
        NativeArray<int> keyArray = tableSheet.KeyArrayNative;  
        if(!keyArray.IsCreated || keyArray.Length == 0)
        {
            table = new Dictionary<int, T>();
            return;
        };
        if (table == null)
        {
            table = new Dictionary<int, T>(keyArray.Length);
        }
        else
        {
            table.Clear();
        }  
        for (var i = 0; i < keyArray.Length; i++)
        {  
            int key = keyArray[i]; 
            T t = new T();
            t.SetRow(i);
            table.Add(key,t);
        }  
    } 
     
}
}

