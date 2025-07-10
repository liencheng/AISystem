using System;
using System.Collections.Generic;
using UnityEngine;
using System.Text.RegularExpressions;
using Unity.Collections;

namespace Games.Table
{ 
    public static class TextDeSerialize
    {
        private static Dictionary<string,int> cacheStringSet = new Dictionary<string, int>();
        private static List<string> stringArray = new List<string>();
        
        private struct FieldInfo
        {
            public string fieldName;
            public int    fieldIndex;
        }

        private struct FieldArray
        {
            public string name;
            public List<FieldInfo> fieldInfos;
        }
        
        
        private static string GetFieldName(string name)
        {
            MatchCollection collection = Regex.Matches(name, @"^[^0-9]+"); 
            foreach (Match o in collection)
            {
                return o.Value;
            }  
            UnityEngine.Debug.LogError($"GetFieldName Error {name}");
            return string.Empty;
        }

        private static void RemoveUnValidChar(ref string value)
        {
            if(value.StartsWith("*"))
            {
                value = value.Substring(1);
            } 
            value = value.Trim();
        }
        private static void SortFieldByNameGroup(List<string> nameArray,ref List<int> validFields)
        {    
            List<int> sortFields = new List<int>();
            List<FieldArray> fieldArray = new List<FieldArray>();  
            for (var i = 0; i < nameArray.Count; i++)
            {
                string name = nameArray[i];
                bool isCombine = false;
                string fieldName = GetFieldName(name);
                foreach (var array in fieldArray)
                {
                    if(array.name == fieldName)
                    {
                        isCombine = true;
                        array.fieldInfos.Add(new FieldInfo(){fieldName = name,fieldIndex = i}); 
                        break;
                    }
                }
                if(!isCombine)
                {
                    fieldArray.Add(new FieldArray(){name = fieldName,fieldInfos = new List<FieldInfo>(){new FieldInfo(){fieldName = name,fieldIndex = i}}});
                } 
            }    
            foreach (var array in fieldArray)
            {
                foreach (var arrayFieldInfo in array.fieldInfos)
                {  
                    sortFields.Add(arrayFieldInfo.fieldIndex);
                }
                // Debug.LogError($"Array {array.name} {array.fieldInfos[0].fieldIndex}");
            }
            validFields.Clear();
            validFields.AddRange(sortFields); 
        }

        private static string[] GetValidFields(string line,ref string[] ignoreArray)
        {
            string[] valueArray = line.TrimEnd('\r').Split('\t');
            List<string> validFields = new List<string>();
            for (var i = 0; i < valueArray.Length; i++)
            {
                if (i == 1 || (i < ignoreArray.Length && ignoreArray[i] == "N"))
                {
                    continue;
                }  
                validFields.Add(valueArray[i]);
            } 
            return validFields.ToArray();
        }

        private static NativeArray<Int32> ToArray(int[] array)
        {
            NativeArray<Int32> nativeArray = new NativeArray<Int32>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<Byte> ToArray(byte[] array)
        {
            NativeArray<Byte> nativeArray = new NativeArray<byte>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<Int16> ToArray(short[] array)
        {
            NativeArray<Int16> nativeArray = new NativeArray<Int16>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<UInt16> ToArray(ushort[] array)
        {
            NativeArray<UInt16> nativeArray = new NativeArray<UInt16>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<Int64> ToArray(long[] array)
        {
            NativeArray<Int64> nativeArray = new NativeArray<Int64>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<Single> ToArray(float[] array)
        {
            NativeArray<Single> nativeArray = new NativeArray<Single>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }
        
        private static NativeArray<Double> ToArray(double[] array)
        {
            NativeArray<Double> nativeArray = new NativeArray<Double>(array.Length, Allocator.Persistent);
            for (var i = 0; i < array.Length; i++)
            {
                nativeArray[i] = array[i];
            }
            return nativeArray;
        }

        private static void StringToNative(List<string> stringList, out NativeArray<byte> byteArray,
            out NativeArray<NativeSlice<byte>> sliceArray)
        {
            int totalLength = 0;
            for (var i = 0; i < stringList.Count; i++)
            {
                totalLength += System.Text.Encoding.UTF8.GetBytes(stringList[i]).Length;
            }
            byteArray = new NativeArray<byte>(totalLength, Allocator.Persistent);
            sliceArray = new NativeArray<NativeSlice<byte>>(stringList.Count, Allocator.Persistent);
            int offset = 0;
            for (var i = 0; i < stringList.Count; i++)
            {
                byte[] bytes = System.Text.Encoding.UTF8.GetBytes(stringList[i]);
                byteArray.Slice(offset, bytes.Length).CopyFrom(bytes);
                sliceArray[i] = byteArray.Slice(offset, bytes.Length);
                offset += bytes.Length;
            }
        }
        
        public static bool  DeSerializeTableSheet(ref TableSheet tableSheet,ref string text)
        {    
            #region 有效表头检查
            text = text.Replace("\r\n", "\r");
            string[] allLines = text.Split('\r'); 
            int startContentToken = -1,typeContentToken = -1;
            for (var i = 0; i < allLines.Length; i++)
            {  
                string line = allLines[i];
                if(line.StartsWith("INT")||line.StartsWith("BYTE")||line.StartsWith("SHORT")||line.StartsWith("LONG")||line.StartsWith("FLOAT")||line.StartsWith("STRING")||line.StartsWith("SLICEBYTE")||line.StartsWith("BOOL")||line.StartsWith("HASHID"))
                {
                    typeContentToken = i;
                } 
                if (!string.IsNullOrEmpty(line) && int.TryParse(line.Substring(0,2), out int var))
                { 
                    startContentToken= i; 
                    break;
                }
            } 
            //校验表格是否合法
            if (allLines.Length < 3 || startContentToken < 2 || typeContentToken < 1)
            { 
                return true;
            } 
            #endregion 有效表头检查

            #region 有效字段检查
            //获取需要忽略的字段
            string[] nameArray = allLines[typeContentToken-1].TrimEnd('\r').Split('\t');
            string[] typeArray = allLines[typeContentToken].TrimEnd('\r').Split('\t');
            string[] ignoreArray;
            if (typeContentToken + 1 < startContentToken)
            {
                ignoreArray = allLines[typeContentToken + 1].TrimEnd('\r').Split('\t');   
            }
            else
            {
                ignoreArray = new string[nameArray.Length];
            }    
            List<int> orginTypeValues = new List<int>();
            List<int> validFields = new List<int>();
            List<int> validRows = new List<int>(); 
            List<string> tmpNameArray = new List<string>();  
            List<string> tmpTypeNameArray = new List<string>();   
            List<int> sortTypeValues = new List<int>();
            int byteCount  =  0,shortCount =  0, intCount   =  0,floatCount =  0,longCount  =  0,stringCount = 0; 
            #endregion 有效字段检查 
       
            #region 生成字段类型
            
            for (var i = 0; i < typeArray.Length; i++)
            {
                if (i == 1 || (i < ignoreArray.Length && ignoreArray[i] == "N"))
                {
                    continue;
                }
                tmpNameArray.Add(nameArray[i]);
                validFields.Add(i); 
                string typeStr = typeArray[i].ToUpper();
                tmpTypeNameArray.Add(typeStr);
                switch (typeStr)
                {
                    case "BYTE":
                    case "BOOL":                        
                        orginTypeValues.Add(byteCount);
                        if(i != 0) byteCount++;
                        break;    
                    case "SHORT":
                        orginTypeValues.Add(1000+shortCount);
                        if(i != 0) shortCount++; 
                        break;                    
                    case "INT":
                    case "HASHID":                         
                        orginTypeValues.Add(2000+intCount);
                        if(i != 0) intCount++;
                        break; 
                    case "LONG":
                    case "INT64":    
                        orginTypeValues.Add(3000+longCount);
                        if(i != 0) longCount++;
                        break;
                    case "FLOAT":
                    case "SINGLE": 
                        orginTypeValues.Add(4000+floatCount);
                        if(i != 0) floatCount++;
                        break;
                    case "STRING":
                    case "SLICEBYTE":     
                        orginTypeValues.Add(5000+stringCount);
                        if(i != 0) stringCount++;
                        break;     
                    default:  
                        UnityEngine.Debug.LogError($"UnSupport Type {typeArray[i]}");
                        tmpTypeNameArray.RemoveAt(tmpTypeNameArray.Count-1);
                        break;
                } 
            }  
            
            #endregion 生成字段类型
            
            #region 生成字段名称
            
            SortFieldByNameGroup(tmpNameArray,ref validFields); 
            
            foreach (var t in validFields)
            {
                sortTypeValues.Add(orginTypeValues[t]);
            }
            
            #endregion 生成字段名称
             
            #region 预处理表格数据
            for (var i = startContentToken; i < allLines.Length; i++)
            {
                string allLine = allLines[i];
                if (!allLine.StartsWith("#") && allLine.Trim().Length > 0 )
                {
                    if(!TableManager.m_LoadClientBlockData && allLine.Contains("（Block）"))
                    {
                        continue;
                    } 
                    validRows.Add(i);
                } 
            }  
            #endregion 预处理表格数据
            
            #region 生成表格数据
            int rowCount = validRows.Count;
            int[]    keyList = new int[rowCount];
            byte[]   byteArray = new byte[byteCount*rowCount];     
            short[]  shortArray = new short[shortCount*rowCount]; 
            int[]    intArray = new int[intCount*rowCount];
            long[]   longArray = new long[longCount*rowCount];
            float[]  floatArray = new float[floatCount*rowCount];  
            int[] stringIndexArray = new int[stringCount*rowCount];
            cacheStringSet.Clear();
            stringArray.Clear(); 
            
            for (var i = 0; i < validRows.Count; i++)
            { 
                string[] valueArray = GetValidFields(allLines[validRows[i]],ref ignoreArray);  
                if(valueArray.Length < 1)
                {
                    continue;
                }
                if(valueArray.Length < validFields.Count)
                {
                    UnityEngine.Debug.LogError($"More Row Error:  {allLines[validRows[i]]} {valueArray.Length} => {validFields.Count}");
                    throw new Exception($"More Row Error:  {allLines[validRows[i]]} {valueArray.Length} => {validFields.Count}");
                    continue;
                } 
                for (var i1 = 0; i1 < validFields.Count; i1++)
                {
                    int fieldIndex = validFields[i1];
                    if (i1 == 0)
                    {
                        if (!int.TryParse(valueArray[fieldIndex], out keyList[i]))
                        {
                            Debug.LogError($"TryParse Error {valueArray[fieldIndex]}");
                            throw new Exception($"TryParse Error {valueArray[fieldIndex]}");
                        }    
                        continue;
                    }
                    int typeVar = orginTypeValues[fieldIndex];
                    if(typeVar < 1000)
                    {
                        string fieldValue = valueArray[fieldIndex];
                        RemoveUnValidChar(ref fieldValue);
                        if (fieldValue.Length == 0)
                        {
                            byteArray[rowCount * typeVar + i] = 0;
                            continue;
                        }
                        if(!int.TryParse(fieldValue,out int tmpValue))
                        {
                            Debug.LogError($"Parse Error {fieldValue} => {typeVar}");
                            throw new Exception($"Parse Error {fieldValue} => {typeVar}");
                            return false;
                        }  
                        if (tmpValue < 0)
                        {
                            //为了兼容特殊的逻辑
                            fieldValue = $"{-tmpValue}";
                        }
                        byteArray[rowCount * typeVar + i] = Convert.ToByte(fieldValue);
                    }
                    else if(typeVar < 2000)
                    { 
                        string fieldValue = valueArray[fieldIndex];
                        RemoveUnValidChar(ref fieldValue);
                        if (fieldValue.Length == 0)
                        {
                            shortArray[rowCount*(typeVar-1000)+i] = 0;
                            continue;
                        }
                        if(!short.TryParse(fieldValue,out shortArray[rowCount*(typeVar-1000)+i]))
                        {
                            Debug.LogError($"Parse Error {fieldValue} => {typeVar}");
                            throw new Exception($"Parse Error {fieldValue} => {typeVar}");
                            return false;
                        }  
                    }
                    else if(typeVar < 3000)
                    {
                        string tmpType = tmpTypeNameArray[fieldIndex];
                        string fieldValue = valueArray[fieldIndex];
                        RemoveUnValidChar(ref fieldValue);
                        if (fieldValue.Length == 0)
                        {
                            intArray[rowCount*(typeVar-2000)+i] = 0;
                            continue;
                        }
                        if(tmpType == "HASHID")
                        {
                            intArray[rowCount * (typeVar - 2000) + i] = TableStringPool.GetStringHashId(valueArray[fieldIndex].Trim());
                        }
                        else
                        {
                            if(!int.TryParse(valueArray[fieldIndex],out intArray[rowCount*(typeVar-2000)+i]))
                            {
                                Debug.LogError($"Parse Error {fieldValue} => {typeVar}");
                                throw new Exception($"Parse Error {fieldValue} => {typeVar}");
                                return false;
                            } 
                        }  
                    }
                    else if(typeVar < 4000)
                    { 
                        string fieldValue = valueArray[fieldIndex];
                        RemoveUnValidChar(ref fieldValue);
                        if (fieldValue.Length == 0)
                        {
                            longArray[rowCount*(typeVar-3000)+i] = 0;
                            continue;
                        }
                        if(!long.TryParse(fieldValue,out longArray[rowCount*(typeVar-3000)+i]))
                        {
                            Debug.LogError($"Parse Error {fieldValue} => {typeVar}");
                            throw new Exception($"Parse Error {fieldValue} => {typeVar}");
                            return false;
                        } 
                    }  
                    else if(typeVar < 5000)
                    {   
                        string fieldValue = valueArray[fieldIndex];
                        RemoveUnValidChar(ref fieldValue);
                        if (fieldValue.Length == 0)
                        {
                            floatArray[rowCount*(typeVar-4000)+i] = 0;
                            continue;
                        }
                        if(!float.TryParse(fieldValue,out floatArray[rowCount*(typeVar-4000)+i]))
                        {
                            throw new Exception($"Parse Error {fieldValue} => {typeVar}");
                            return false;
                        } 
                    }
                    else if (typeVar < 6000)
                    { 
                        string tmpStr = valueArray[fieldIndex];
                        int checkIndexRange = (rowCount * (typeVar - 5000) + i);  
                        if (cacheStringSet.TryGetValue(tmpStr, out int index))
                        {
                            stringIndexArray[checkIndexRange] = index;
                        }
                        else
                        { 
                            int appendIndex = stringArray.Count;
                            cacheStringSet[tmpStr] = appendIndex;
                            stringIndexArray[checkIndexRange] = appendIndex;
                            stringArray.Add(tmpStr);
                        } 
                    } 
                }
            } 
            #endregion 生成表格数据 
             
            #region 填充表数据
            //剔除Key字段 需要进行重新排序  
            sortTypeValues.RemoveAt(0); 
            tableSheet.RowCount = rowCount;
            tableSheet.FiledTypesNative = ToArray(sortTypeValues.ToArray()); 
            tableSheet.KeyArrayNative = ToArray(keyList); 
            tableSheet.ByteArrayNative = ToArray(byteArray);
            tableSheet.ShortArrayNative = ToArray(shortArray);
            tableSheet.IntArrayNative = ToArray(intArray);
            tableSheet.LongArrayNative = ToArray(longArray); 
            tableSheet.FloatArrayNative= ToArray(floatArray);

            StringToNative(stringArray, out tableSheet.StringByteArrayNative, out tableSheet.StringSliceNative); 
            
            tableSheet.StringLargeIndex = ushort.MaxValue <= stringArray.Count;
            if (tableSheet.StringLargeIndex)
            { 
                tableSheet.StringIndexIntNative = ToArray(stringIndexArray);
            }
            else
            { 
                ushort [] stringIndexUShort = new ushort[stringIndexArray.Length]; 
                for (var i = 0; i < stringIndexArray.Length; i++)
                {
                    stringIndexUShort[i] = (ushort)stringIndexArray[i];
                } 
                tableSheet.StringIndexShortNative = ToArray(stringIndexUShort);
            } 
            tableSheet.ResetDataSize();
            stringArray.Clear();
            cacheStringSet.Clear();
            #endregion 填充表数据 
            return true; 
        }
    } 
}

