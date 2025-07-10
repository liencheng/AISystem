using System.Collections.Generic;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;
using UnityEngine;

namespace Games.Table
{
    public class TableSheet
    {
        private static readonly BinaryDeserialize BinaryDeserialize = new BinaryDeserialize();
        private static BinarySerialize   _binarySerialize; 
 
        public bool     StringLargeIndex;  
        public int      RowCount;   
        public int      AccessTime; 
        
        private int _keyArrayCount; 
        private int _byteArrayCount;
        private int _shortArrayCount;
        private int _intArrayCount;
        private int _floatArrayCount;
        private int _longArrayCount; 
        private int _stringIndexShortCount;
        private int _stringIndexIntCount;
        
        public NativeArray<int> KeyArrayNative;
        public NativeArray<int> FiledTypesNative;
        public NativeArray<byte> ByteArrayNative;
        public NativeArray<short> ShortArrayNative;
        public NativeArray<int>   IntArrayNative;
        public NativeArray<float> FloatArrayNative;
        public NativeArray<long> LongArrayNative;
        public NativeArray<ushort> StringIndexShortNative; 
        public NativeArray<int> StringIndexIntNative;
        public NativeArray<byte> StringByteArrayNative;
        public NativeArray<NativeSlice<byte>> StringSliceNative;
        private Dictionary<int, HashSliceByte> _stringHashMap = new Dictionary<int, HashSliceByte>();


        public void ResetDataSize()
        {
            AccessTime = 0;
            foreach (var keyValuePair in _stringHashMap)
            {
                HashSliceByte sliceByte = keyValuePair.Value;
                TableStringPool.RemoveGlobalString(ref sliceByte);            
            } 
            _stringHashMap.Clear();
            if (KeyArrayNative.IsCreated)
            {
                _keyArrayCount = KeyArrayNative.Length;
            } 
            if (ByteArrayNative.IsCreated)
            { 
                _byteArrayCount = ByteArrayNative.Length;
            }
            if (ShortArrayNative.IsCreated)
            {
                _shortArrayCount = ShortArrayNative.Length;
            }
            if (IntArrayNative.IsCreated)
            {
                _intArrayCount = IntArrayNative.Length;
            }
            if (FloatArrayNative.IsCreated)
            {
                _floatArrayCount = FloatArrayNative.Length;
            }
            if(LongArrayNative.IsCreated)
            {
                _longArrayCount = LongArrayNative.Length;
            }
            if(StringIndexShortNative.IsCreated)
            {
                _stringIndexShortCount = StringIndexShortNative.Length;
            }
            if(StringIndexIntNative.IsCreated)
            {
                _stringIndexIntCount = StringIndexIntNative.Length;
            } 
        }
        
        
        private const int IntType   = 1000;

        public void Dispose()
        {
            AccessTime = 0;
            if (_stringHashMap != null)
            {
                foreach (var keyValuePair in _stringHashMap)
                {
                    HashSliceByte sliceByte = keyValuePair.Value;
                    TableStringPool.RemoveGlobalString(ref sliceByte);            
                } 
                _stringHashMap.Clear();
            } 
            
            if (KeyArrayNative.IsCreated)
            {
                KeyArrayNative.Dispose();
            }
            if (FiledTypesNative.IsCreated)
            {
                FiledTypesNative.Dispose();
            }
            if (ByteArrayNative.IsCreated)
            {
                ByteArrayNative.Dispose();
            }
            if (ShortArrayNative.IsCreated)
            {
                ShortArrayNative.Dispose();
            }
            if (IntArrayNative.IsCreated)
            {
                IntArrayNative.Dispose();
            }
            if (FloatArrayNative.IsCreated)
            {
                FloatArrayNative.Dispose();
            }
            if(LongArrayNative.IsCreated)
            {
                LongArrayNative.Dispose();
            }
            if(StringIndexShortNative.IsCreated)
            {
                StringIndexShortNative.Dispose();
            }
            if(StringIndexIntNative.IsCreated)
            {
                StringIndexIntNative.Dispose();
            }
            if(StringByteArrayNative.IsCreated)
            {
                StringByteArrayNative.Dispose();
            }
            if(StringSliceNative.IsCreated)
            {
                StringSliceNative.Dispose();
            }  
            _stringHashMap?.Clear();
            _stringHashMap = null;
        }
        
        public static bool LoadBinarySheet(byte[] bytes,out TableSheet tableSheet)
        {  
             tableSheet = new TableSheet();
            BinaryDeserialize.ReSet(bytes);
            bool result = BinaryDeserialize.DeSerializeTableSheet(ref tableSheet);
            BinaryDeserialize.Clean(); 
            return result; 
        }

        public static bool LoadTextSheet(string text,out TableSheet tableSheet)
        {
            tableSheet = new TableSheet(); 
            bool result = TextDeSerialize.DeSerializeTableSheet(ref tableSheet,ref text);
            #if TABLE_STRING_HASH_TEST
            if (result)
            {
                tableSheet.CheckAllStringHash();
            } 
            #endif
            return result;
        } 
        
        public void SaveBinarySheet(string tableName)
        {
            _binarySerialize ??= new BinarySerialize(); 
            _binarySerialize.SerializeSheet(this);
            byte[] bytes = _binarySerialize.GetBytes();
            string assetPath;
    #if UNITY_EDITOR 
            assetPath = $"{Application.dataPath}/Game/Bundle/Table/Tab_{tableName}_Data.bytes";
    #else    
            assetPath = $"{Application.persistentDataPath}/ResData/zh/Table/Tab_{tableName}_Data.bytes"; 
    #endif
            if (!string.IsNullOrEmpty(assetPath))
            {
                Utils.CreateTableTextAsset(assetPath, bytes);           
            } 
            _binarySerialize.Clean();  
        }

        public int GetKey(int rowIndex)
        {
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetKey");
            if (0 < _keyArrayCount && 0 <= rowIndex && rowIndex < _keyArrayCount)
            { 
                return KeyArrayNative[rowIndex];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return -1; 
        }
        
        public int GetInt( int rowIndex, int fieldIndex)
        {
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetInt");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            if (0 < _intArrayCount && 0 <= index && index < _intArrayCount)
            { 
                return IntArrayNative[index];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return 0;
        }

        public bool GetBool(int rowIndex, int fieldIndex)
        { 
            return GetByte(rowIndex, fieldIndex) != 0;
        }
         
        
        public byte GetByte(int rowIndex, int fieldIndex)
        { 
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetByte");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            if (0 < _byteArrayCount && 0 <= index &&  index < _byteArrayCount)
            {
                return ByteArrayNative[index];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return 0;
        }

        public short GetShort(int rowIndex, int fieldIndex)
        {
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetShort");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            if ( 0 < _shortArrayCount  && index < _shortArrayCount && 0 <= index)
            {
                return ShortArrayNative[index];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return 0;
        } 
        
        public float GetFloat(int rowIndex, int fieldIndex)
        {  
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetFloat");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            if (0 < _floatArrayCount && index < _floatArrayCount && 0 <= index)
            {
                return FloatArrayNative[index];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return 0;
        }  
        public long GetLong(int rowIndex, int fieldIndex)
        {  
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetLong");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            if (0 < _longArrayCount && index < _longArrayCount && 0 <= index)
            {
                return LongArrayNative[index];
            }
            // UnityEngine.Profiling.Profiler.EndSample();
            return 0;
        }   
        public string GetString(int rowIndex, int fieldIndex)
        { 
            AccessTime = GameManager.FrameCount;
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetString");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            int stringIndex = -1;
            if (StringLargeIndex)
            {
                if (0 < _stringIndexIntCount && index < _stringIndexIntCount && 0 <= index)
                {
                    stringIndex = StringIndexIntNative[index];
                }
            }
            else
            {
                if (0 < _stringIndexShortCount && index < _stringIndexShortCount && 0 <= index)
                {
                    stringIndex = StringIndexShortNative[index];
                }
            }
            if(stringIndex == -1) return string.Empty; 
            
            if(_stringHashMap.TryGetValue(stringIndex,out HashSliceByte hashCode) && TableStringPool.GetGlobalString(hashCode,out string newString) )  
            {
                return newString;
            }  
            NativeSlice<byte> slice = StringSliceNative[stringIndex];
            if(slice.Length == 0) return string.Empty;  
            
            _stringHashMap[stringIndex] = TableStringPool.GetSliceString(ref slice, out string newString2); 
            // UnityEngine.Profiling.Profiler.EndSample();
            return newString2;   
        }     
        
        public NativeSlice<byte> GetNativeSliceByte(int rowIndex, int fieldIndex)
        {
            AccessTime = GameManager.FrameCount; 
            // UnityEngine.Profiling.Profiler.BeginSample("TableSheet GetSliceByte");
            int index = RowCount * (FiledTypesNative[fieldIndex] % IntType) + rowIndex;
            int stringIndex = -1;
            if (StringLargeIndex)
            {
                if (0 < _stringIndexIntCount && index < _stringIndexIntCount && 0 <= index)
                {
                    stringIndex = StringIndexIntNative[index];
                }
            }
            else
            {
                if (0 < _stringIndexShortCount && index < _stringIndexShortCount && 0 <= index)
                {
                    stringIndex = StringIndexShortNative[index];
                }
            }
            if(stringIndex == -1) return new NativeSlice<byte>(); 
            // UnityEngine.Profiling.Profiler.EndSample(); 
            return StringSliceNative[stringIndex];  
        }
        
        /// <summary>
        /// 专门用于Hash碰撞测试测试的 不要在Release版本中使用 
        /// </summary>
        private void CheckAllStringHash()
        {
            Dictionary<uint,List<string>> cacheMap = new Dictionary<uint, List<string>>();
            for (int i = 0; i < StringSliceNative.Length; i++)
            { 
                NativeSlice<byte> slice = StringSliceNative[i];
                if (slice.Length != 0)
                {
                    HashSliceByte hashSlice =  TableStringPool.GetSliceString(ref slice, out string globalString);
                    if(cacheMap.TryGetValue(hashSlice.GetHashCodeUInt(), out List<string> list))
                    {
                        list.Add(System.Text.Encoding.UTF8.GetString(slice.ToArray()));
                    }
                    else
                    {
                        cacheMap[hashSlice.GetHashCodeUInt()] = new List<string> { System.Text.Encoding.UTF8.GetString(slice.ToArray()) };
                    }  
                }  
            } 
            foreach (var keyValuePair in cacheMap)
            {
                if (0 < keyValuePair.Value.Count)
                { 
                    string first = keyValuePair.Value[0];
                    for (int i = 1; i < keyValuePair.Value.Count; i++)
                    {
                        if (first != keyValuePair.Value[i])
                        {
                            Debug.LogError($"CheckAllStringHash Error HashId   {keyValuePair.Key}  => {first}  !=  {keyValuePair.Value[i]}");
                            break;
                        }
                    } 
                } 
            }
        } 
    }
}

