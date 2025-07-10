using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;
using Games.Table;
using UnityEngine;

namespace Games.Table
{
    public class StructMethodAccessor
    { 
        public string FieldName;
        public MethodInfo FieldMethodName;
        public bool isArray;  
        public MethodInfo FieldCountName; 
    } 


    public class StructTableToString
    {
        public static string TableToString<T>(string tableName,Dictionary<int, T> dictionary) where T : ITable
        {
            MethodInfo[] methodInfos = typeof(T).GetMethods(System.Reflection.BindingFlags.Instance |
                                                            System.Reflection.BindingFlags.Public);
            Dictionary<string, StructMethodAccessor> fieldNames = new Dictionary<string, StructMethodAccessor>();

            //扫描并排序所有方法
            foreach (var method in methodInfos)
            {
                string propertyName = method.Name;
                if (propertyName.Equals("IsNull") || propertyName.Equals("IsNotNull") || propertyName.Equals("IsEqual") || propertyName.Equals("SetRow") || 
                    propertyName.Equals("Equals") || propertyName.Equals("GetHashCode") || propertyName.Equals("GetType") ||
                    propertyName.Equals("ToString"))
                {
                    continue;
                }

                if (propertyName.StartsWith("get_"))
                {
                    string fieldName = propertyName.Replace("get_", "");
                    fieldNames.Add(fieldName, new StructMethodAccessor()
                    {
                        FieldName = fieldName,
                        FieldMethodName = method,
                        isArray = false
                    });
                }else if (propertyName.StartsWith("get") && propertyName.EndsWith("Count"))
                {
                    string fieldName = propertyName.Substring(3, propertyName.Length - 3); 
                    fieldName = fieldName.Substring(0, fieldName.Length - 5); 
                    if (fieldNames.TryGetValue(fieldName, out StructMethodAccessor accessor))
                    {
                        accessor.FieldCountName = method;
                    }
                    else
                    {
                        fieldNames.Add(fieldName, new StructMethodAccessor()
                        {
                            FieldName = fieldName,
                            isArray = true,
                            FieldCountName = method
                        });
                    }
                }
                else if (propertyName.StartsWith("Get") && propertyName.EndsWith("byIndex"))
                {
                    string fieldName = propertyName.Substring(3, propertyName.Length - 3); 
                    fieldName = fieldName.Substring(0, fieldName.Length - 7);
                    if (fieldNames.TryGetValue(fieldName, out StructMethodAccessor accessor))
                    {
                        accessor.FieldMethodName = method;
                    }
                    else
                    {
                        fieldNames.Add(fieldName, new StructMethodAccessor()
                        {
                            FieldName = fieldName,
                            isArray = true,
                            FieldMethodName = method
                        });
                    }
                } 
            }

            StringBuilder builder = new StringBuilder(); 
            
            foreach (var fieldPairs in fieldNames)
            {
                builder.Append(fieldPairs.Key + "\t");
            } 
            builder.AppendLine(""); 
            
            foreach (var keyValuePair in dictionary)
            {
                foreach (var fieldPairs in fieldNames)
                {
                    try
                    {
                        StructMethodAccessor accessor = fieldPairs.Value;
                        if (accessor.isArray)
                        {
                            if(accessor.FieldCountName == null || accessor.FieldMethodName == null)
                            { 
                                Debug.LogError($"accessor {accessor.FieldName}  FieldMethodName or FieldCountName is null"); 
                            }
                            StringBuilder stringBuilder = new StringBuilder(); 
                            int count = (int)accessor.FieldCountName.Invoke(keyValuePair.Value, null);
                            for (int i = 0; i < count; i++)
                            {
                                stringBuilder.Append(accessor.FieldMethodName.Invoke(keyValuePair.Value, new object[] { i })+" "); 
                            } 
                            builder.Append(stringBuilder.ToString()+"\t");
                        }
                        else
                        {
                            if(accessor.FieldMethodName == null)
                            { 
                                Debug.LogError($"accessor {accessor.FieldName}  FieldMethodName is null"); 
                            } 
                            builder.Append(accessor.FieldMethodName.Invoke(keyValuePair.Value, null)+"\t"); 
                        }
                    }
                    catch (Exception e)
                    {
                        Debug.LogError($"{keyValuePair.Key}  {fieldPairs.Key} {e.Message}");
                    } 
                } 
                builder.AppendLine("");
            } 
            
            return builder.ToString();   
        }  
    }
    
}

