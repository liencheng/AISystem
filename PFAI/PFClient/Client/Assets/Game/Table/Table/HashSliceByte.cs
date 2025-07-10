using System;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;

namespace Games.Table
{
    public struct HashSliceByte
    {
        private readonly uint     _hashCode; 
        private NativeSlice<byte> _nativeData;
        
        public HashSliceByte(uint hashCode, NativeSlice<byte> data)
        {
            _hashCode = hashCode;  
            _nativeData = data;
        } 
         
        public override bool Equals(object obj)
        {
            if (obj is HashSliceByte other && _hashCode == other._hashCode && _nativeData.Length == other._nativeData.Length)
            {   
                // Compare the byte arrays
                for (int i = 0; i < _nativeData.Length; i++)
                {
                    if (_nativeData[i] != other._nativeData[i])
                        return false;
                }
                return true;
            } 
            return false;
        }
        
        
        public override int GetHashCode()
        {
            return (int)_hashCode;
        }
        
        public uint GetHashCodeUInt()
        {
            return _hashCode;
        }
        
    }
}