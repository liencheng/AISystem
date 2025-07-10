using System;  
using System.Text;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;
using UnityEngine;

namespace Games.Table
{
    public struct TableFieldMask
    {
        public const byte Byte = 1;
        public const byte Short = 2;
        public const byte Int = 4;
        public const byte Long = 8;
        public const byte Float = 16;
        public const byte String = 32;
    }
    public class BinaryDeserialize
    {
        
        
        private const byte Version = 1;
        private byte[] _buffer; 
        private int _index;

        public BinaryDeserialize()
        {
        }
        
        public void ReSet(byte[] bytes)
        {
            _buffer = bytes;
            _index = 0;
        }

        public void Clean()
        {
            _buffer = null;
            _index = 0;
        }
 
        /// <summary>
        /// 获取字符串
        /// </summary>
        /// <returns></returns>
        private string GetString()
        {
            if (_buffer == null)
                return "";
            if (_buffer.Length < _index + sizeof(int))
                return "";
            int strLen = BitConverter.ToInt32(_buffer, _index);
            if (_buffer.Length < _index + sizeof(int) + strLen)
                return "";
            string str = Encoding.UTF8.GetString(_buffer, _index + sizeof(int), strLen);
            _index = _index + sizeof(int) + strLen;
            return str;
        }
 

        private short GetShort()
        {
            if (_buffer == null)
                return 0;
            if (_buffer.Length < _index + 2)
                return 0; 
            return (short)(_buffer[_index++] | _buffer[_index++] << 8); 
        } 
        
        private ushort GetUShort()
        {
            if (_buffer == null)
                return 0;
            if (_buffer.Length < _index + 2)
                return 0; 
            return (ushort)(_buffer[_index++] | _buffer[_index++] << 8); 
        } 

        

        /// <summary>
        /// 将字节数组转化成Int32
        /// </summary> 
        private int GetInt32()
        {
            if (_buffer == null)
                return 0;
            if (_buffer.Length < _index + 4)
                return 0; 
            return (int)(_buffer[_index++] | _buffer[_index++] << 8 | _buffer[_index++] << 16 | _buffer[_index++] << 24);
        }

        /// <summary>
        /// 将字节数组转化成Int64
        /// </summary> 
        private long GetInt64()
        {
            if (_buffer == null)
                return 0;
            if (_buffer.Length < _index + 8)
                return 0; 
            
            long value = BitConverter.ToInt64(_buffer, _index);
            _index += 8;
            return value;
        }

        /// <summary>
        /// 将字节数组转化成float
        /// </summary> 
        private unsafe float GetFloat()
        {
            if (_buffer == null)
                return -1;
            if (_buffer.Length < _index + sizeof(float))
                return -1;
            uint temp = (uint)(_buffer[_index++] | _buffer[_index++] << 8 | _buffer[_index++] << 16 | _buffer[_index++] << 24);
            return *((float*)&temp);
        }

        /// <summary>
        /// 将字节数组转化成double
        /// </summary> 
        private unsafe double GetDouble()
        {
            if (_buffer == null)
                return -1;
            if (_buffer.Length < _index + sizeof(float))
                return -1; 
             
            uint lo = (uint)(_buffer[_index++] | _buffer[_index++] << 8 | _buffer[_index++] << 16 | _buffer[_index++] << 24);
            uint hi = (uint)(_buffer[_index++] | _buffer[_index++] << 8 | _buffer[_index++] << 16 | _buffer[_index++] << 24);
            ulong temp = ((ulong)hi) << 32 | lo;

            return *((double*)&temp);
        }
 
        private bool GetBoolean()
        {
            return (_buffer[_index++] == 1);
        }

        private byte GetByte()
        {
            return (byte)_buffer[_index++];
        }

        private byte[] GetByteArray()
        {
            int arrayLen = GetInt32(); 
            byte[] tmpArray = new byte[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = _buffer[_index++];
            } 
            return tmpArray;
        }
        
        private NativeArray<byte> GetNativeByteArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<byte> tmpArray = new NativeArray<byte>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = _buffer[_index++];
            } 
            return tmpArray;
        }
        
        

        private short[] GetShortArray()
        {
            int arrayLen = GetInt32(); 
            short[] tmpArray = new short[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetShort();
            } 
            return tmpArray;
        }
        
        private NativeArray<short> GetNativeShortArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<short> tmpArray = new NativeArray<short>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetShort();
            } 
            return tmpArray;
        }
          
        
        private ushort[] GetUShortArray()
        {
            int arrayLen = GetInt32(); 
            ushort[] tmpArray = new ushort[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetUShort();
            } 
            return tmpArray;
        }
        
        private NativeArray<ushort> GetNativeUShortArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<ushort> tmpArray = new NativeArray<ushort>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetUShort();
            } 
            return tmpArray;
        }
        
        
        private int[] GetInt32Array()
        {
            int arrayLen = GetInt32(); 
            int[] tmpArray = new int[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetInt32();
            } 
            return tmpArray;
        }
        
        private NativeArray<int> GetNativeIntArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<int> tmpArray = new NativeArray<int>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetInt32();
            } 
            return tmpArray;
        }

        private long[] GetInt64Array()
        {
            int arrayLen = GetInt32(); 
            long[] tmpArray = new long[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetInt64();
            } 
            return tmpArray; 
        }
        
        private NativeArray<long> GetNativeLongArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<long> tmpArray = new NativeArray<long>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetInt64();
            } 
            return tmpArray; 
        }

        private float[] GetFloatArray()
        {
            int arrayLen = GetInt32(); 
            float[] tmpArray = new float[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetFloat();
            } 
            return tmpArray;  
        }
        
        private NativeArray<float> GetNativeFloatArray()
        {
            int arrayLen = GetInt32(); 
            NativeArray<float> tmpArray = new NativeArray<float>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetFloat();
            } 
            return tmpArray;  
        }

        private double[] GetDoublesArray()
        { 
            int arrayLen = GetInt32(); 
            double[] tmpArray = new double[arrayLen];
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetDouble();
            } 
            return tmpArray;  
        }
        
        private NativeArray<double> GetNativeDoublesArray()
        { 
            int arrayLen = GetInt32(); 
            NativeArray<double> tmpArray = new NativeArray<double>(arrayLen, Allocator.Persistent);
            for (int i = 0; i < arrayLen; i++)
            {
                tmpArray[i] = GetDouble();
            } 
            return tmpArray;  
        }

  
        
        private void GetStringNativeArray(out NativeArray<byte> byteArray,out NativeArray<NativeSlice<byte>> stringArray)
        {
            int arrayLen = GetInt32(); 
            int byteLen  = GetInt32();
            stringArray = new NativeArray<NativeSlice<byte>>(arrayLen, Allocator.Persistent);
            byteArray = new NativeArray<byte>(byteLen, Allocator.Persistent);  
            unsafe
            {
              byte* source = (byte*)byteArray.GetUnsafePtr();
              if (source == null)
              {
                Debug.LogError("GetStringNativeArray source is null");
                return;
              }
              int byteIndex = 0;
              int offSet = sizeof(int); 
              int bufferLen = _buffer.Length;
              for (int i = 0; i < arrayLen; i++)
              {
                  int strLen = BitConverter.ToInt32(_buffer, _index);
                  try
                  {   
                      if (0 < strLen && _index + offSet < bufferLen)
                      {
                          fixed(byte* p = &_buffer[_index + offSet])
                          { 
                              UnsafeUtility.MemCpy(source + byteIndex,  p, strLen); 
                          }  
                      } 
                      stringArray[i] = new NativeSlice<byte>(byteArray, byteIndex, strLen);
                      byteIndex += strLen;
                      _index += (offSet + strLen);
                  }
                  catch (Exception e)
                  {
                      Debug.LogError($"GetStringNativeArray MemCpy Error: {e} {_buffer.Length} {_index} {byteIndex}");
                      return;
                  }  
              }
              source = null;
            }  
        }

        public bool DeSerializeTableSheet(ref TableSheet tableSheet)
        {  
            byte readerVersion = GetByte();
            if (readerVersion != Version)
            {
                Debug.LogError($"SerializeVersion Error {readerVersion} : {Version}"); 
                return false;
            } 
            tableSheet.RowCount   = GetInt32();
            tableSheet.KeyArrayNative = GetNativeIntArray();
            tableSheet.FiledTypesNative = GetNativeIntArray();  
            byte valueMask = GetByte();
            if ((valueMask & TableFieldMask.Byte) == TableFieldMask.Byte)
            {
                tableSheet.ByteArrayNative = GetNativeByteArray(); 
            }
            if ((valueMask & TableFieldMask.Short) == TableFieldMask.Short)
            {
                tableSheet.ShortArrayNative = GetNativeShortArray(); 
            }
            if ((valueMask & TableFieldMask.Int) == TableFieldMask.Int)
            {
                tableSheet.IntArrayNative = GetNativeIntArray(); 
            }
            if ((valueMask & TableFieldMask.Long) == TableFieldMask.Long)
            {
                tableSheet.LongArrayNative = GetNativeLongArray(); 
            }  
            if ((valueMask & TableFieldMask.Float) == TableFieldMask.Float)
            {
                tableSheet.FloatArrayNative = GetNativeFloatArray(); 
            }  
            if ((valueMask & TableFieldMask.String) == TableFieldMask.String)
            {
                tableSheet.StringLargeIndex = GetByte() == 1;
                if (tableSheet.StringLargeIndex)
                { 
                    tableSheet.StringIndexIntNative = GetNativeIntArray(); 
                }
                else
                {
                    tableSheet.StringIndexShortNative = GetNativeUShortArray(); 
                }  
                GetStringNativeArray(out tableSheet.StringByteArrayNative, out tableSheet.StringSliceNative); 
            } 
            tableSheet.ResetDataSize();
            return true;
        }  
} 
}

