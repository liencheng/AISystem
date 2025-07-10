using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Unity.Collections;
using UnityEngine;

namespace Games.Table
{
    public class BinarySerialize
    { 
        private const byte Version = 1;
        
        private List<byte> _buffer;

        public BinarySerialize()
        {
            _buffer = new List<byte>();
        }

        ~BinarySerialize()
        {
            Clean();
            _buffer = null;
        }

        public void Clean()
        {
            if (_buffer != null)
            {
                _buffer.Clear();
            } 
        }

        public byte[] GetBytes()
        {
            byte[] tmpBytes = _buffer.ToArray();
            _buffer.Clear();
            return tmpBytes; 
        }

        private void SetByte(byte value)
        {
            _buffer.Add((byte)value);
        } 
        
        private void SetShort(short value)
        { 
            _buffer.AddRange(BitConverter.GetBytes(value));   
        } 
        
        private void SetUShort(ushort value)
        { 
            _buffer.AddRange(BitConverter.GetBytes(value));  
        } 
        
        private void SetInt32(int value)
        {  
            _buffer.AddRange(BitConverter.GetBytes(value));  
        }

        private void SetInt64(long value)
        { 
            _buffer.AddRange(BitConverter.GetBytes(value)); 
        }

        private void SetFloat(float value)
        {
            _buffer.AddRange(BitConverter.GetBytes(value));  
        }

        private unsafe void SetDouble(double value)
        {
            _buffer.AddRange(BitConverter.GetBytes(value));   
        }

        private void SetString(string value)
        {
            try
            {
                byte[] strBytes = Encoding.UTF8.GetBytes(value);
                int len = strBytes.Length;
                byte[] lenBytes = BitConverter.GetBytes(len);
                _buffer.AddRange(lenBytes);
                _buffer.AddRange(strBytes);
            }
            catch (System.Exception e)
            { 
                Debug.LogError("SetString => "+value+" => "+e.Message+" => "+e.StackTrace);
                throw;
            } 
        }

        private void SetBool(bool value)
        {
            _buffer.Add((byte)(value ? 1 : 0));
        }
        
        
        private void SetByteArray(NativeArray<byte> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            _buffer.AddRange(array);
        }

        private void SetShortArray(NativeArray<short> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetShort(i);
            }
        }
        
        private void SetUShortArray(NativeArray<ushort> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetUShort(i);
            }
        }

        
        private void SetInt32Array(NativeArray<int> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetInt32(i);
            }
        }

        private void SetInt64Array(NativeArray<long> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetInt64(i);
            }
        }

        private void SetFloatArray(NativeArray<float> array)
        {
            if (array.Length == 0 || !array.IsCreated) 
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetFloat(i);
            }
        }  
        

        private void SetByteArray(byte[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            _buffer.AddRange(array);
        }

        private void SetShortArray(short[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetShort(i);
            }
        }
        
        private void SetUShortArray(ushort[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetUShort(i);
            }
        }

        
        private void SetInt32Array(int[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetInt32(i);
            }
        }

        private void SetInt64Array(long[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetInt64(i);
            }
        }

        private void SetFloatArray(float[] array)
        {
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetFloat(i);
            }
        } 

        private void SetStringArray(string[] array)
        { 
            if (array == null)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(array.Length);
            foreach (var i in array)
            {
                SetString(i);
            }
        }
        
        private void SetStringNativeArray(ref NativeArray<byte> byteArray,ref NativeArray<NativeSlice<byte>> sliceArray)
        { 
            if(!byteArray.IsCreated || byteArray.Length == 0)
            {
                SetInt32(0);
                return;
            } 
            SetInt32(sliceArray.Length);
            SetInt32(byteArray.Length); 
            foreach (var nativeSlice in sliceArray)
            { 
                _buffer.AddRange(BitConverter.GetBytes(nativeSlice.Length));
                _buffer.AddRange(nativeSlice.ToArray());
            }   
        }

        public void SerializeSheet(TableSheet tableSheet)
        {
            Clean(); 
            SetByte(Version); 
            SetInt32(tableSheet.RowCount);
            SetInt32Array(tableSheet.KeyArrayNative);
            SetInt32Array(tableSheet.FiledTypesNative);
            byte valueMask = 0;
            if (tableSheet.ByteArrayNative.IsCreated && 0 < tableSheet.ByteArrayNative.Length)
            {
                valueMask|=1;
            } 
            if (tableSheet.ShortArrayNative.IsCreated && 0 < tableSheet.ShortArrayNative.Length)
            {
                valueMask|=2;
            } 
            if (tableSheet.IntArrayNative.IsCreated && 0 < tableSheet.IntArrayNative.Length)
            {
                valueMask|=4;
            }
            if (tableSheet.LongArrayNative.IsCreated && 0 < tableSheet.LongArrayNative.Length)
            {
                valueMask|=8;
            }
            if (tableSheet.FloatArrayNative.IsCreated && 0 < tableSheet.FloatArrayNative.Length)
            {
                valueMask|=16;
            }
            if (tableSheet.StringByteArrayNative.IsCreated && 0 < tableSheet.StringByteArrayNative.Length)
            {
                valueMask|=32;
            }  
            SetByte(valueMask);
            if (tableSheet.ByteArrayNative.IsCreated && 0 < tableSheet.ByteArrayNative.Length)
            {  
                SetByteArray(tableSheet.ByteArrayNative); 
            } 
            if (tableSheet.ShortArrayNative.IsCreated && 0 < tableSheet.ShortArrayNative.Length)
            {  
                SetShortArray(tableSheet.ShortArrayNative); 
            } 
            if (tableSheet.IntArrayNative.IsCreated && 0 < tableSheet.IntArrayNative.Length)
            {
                SetInt32Array(tableSheet.IntArrayNative); 
            }
            if (tableSheet.LongArrayNative.IsCreated && 0 < tableSheet.LongArrayNative.Length)
            {
                SetInt64Array(tableSheet.LongArrayNative); 
            }
            if (tableSheet.FloatArrayNative.IsCreated && 0 < tableSheet.FloatArrayNative.Length)
            {
                SetFloatArray(tableSheet.FloatArrayNative); 
            } 
            if(tableSheet.StringByteArrayNative.IsCreated && 0 < tableSheet.StringByteArrayNative.Length)
            {    
                SetByte(tableSheet.StringLargeIndex ? (byte)1 : (byte)0);
                if (tableSheet.StringLargeIndex)
                {
                    SetInt32Array(tableSheet.StringIndexIntNative); 
                }
                else
                {
                    SetUShortArray(tableSheet.StringIndexShortNative); 
                }
                SetStringNativeArray(ref tableSheet.StringByteArrayNative,ref tableSheet.StringSliceNative); 
            }  
        }   
    } 
}
 
