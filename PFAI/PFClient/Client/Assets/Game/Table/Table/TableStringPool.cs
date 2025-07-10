using System.Collections.Generic;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;

namespace Games.Table
{
    public class TableStringPool
    {
        private static Dictionary<HashSliceByte, string> _strDictionary = new Dictionary<HashSliceByte, string>();
  
        public static void RemoveGlobalString(ref HashSliceByte sharedHashId)
        { 
            if (_strDictionary.Count > 0 && !_strDictionary.Remove(sharedHashId))
            {
                UnityEngine.Debug.LogError($"RemoveGlobalString Error! {sharedHashId}");
            }
        } 
        public static bool GetGlobalString(HashSliceByte sharedHashId,out string globalString)
        {
            return _strDictionary.TryGetValue(sharedHashId, out globalString);
        }
        
        public static unsafe HashSliceByte GetSliceString(ref NativeSlice<byte> slice,out string globalString)
        {
            if (slice.Length == 0)
            {
                globalString = string.Empty;
                return new HashSliceByte(0, slice);
            }
            uint hashId = GetSliceHashId(ref slice);
            HashSliceByte hashSliceByte = new HashSliceByte(hashId, slice); 
            if (_strDictionary.TryGetValue(hashSliceByte, out globalString))
            {
                return hashSliceByte;
            }
            byte* chPtr = (byte*)slice.GetUnsafePtr();
            if(chPtr == null)
            {
                globalString = string.Empty;
                UnityEngine.Debug.LogError($"GetSliceString Error! {hashId}"); 
                return new HashSliceByte(0, slice);
            }
            globalString = System.Text.Encoding.UTF8.GetString(chPtr, slice.Length);
            _strDictionary.Add(hashSliceByte, globalString);
            return hashSliceByte; 
        }
        
        public static void ClearGlobalString()
        {
            _strDictionary.Clear();
        }

        public static void Dispose()
        {
            ClearGlobalString();
        }
          
        private static unsafe uint GetSliceHashId(ref NativeSlice<byte> slice)
        {
            byte* chPtr = (byte*)slice.GetUnsafePtr();
            int num1 = 352654597;
            int num2 = num1;
            int* numPtr = (int*)chPtr;
            int length;
            for (length = slice.Length; length > 1; length -= 2)
            {
                num1 = (num1 << 5) + num1 + (num1 >> 27) ^ *numPtr;
                num2 = (num2 << 5) + num2 + (num2 >> 27) ^ numPtr[1];
                numPtr += 2;
            } 
            if (length > 0)
                num1 = (num1 << 5) + num1 + (num1 >> 27) ^ *numPtr;
            return (uint)(num1 + num2 * 1566083941); 
        }

        public static unsafe int GetStringHashId(string originString)
        {
            fixed (char* chPtr = originString)
            {
                int num1 = 352654597;
                int num2 = num1;
                int* numPtr = (int*) chPtr;
                int length;
                for (length = originString.Length; length > 2; length -= 4)
                {
                    num1 = (num1 << 5) + num1 + (num1 >> 27) ^ *numPtr;
                    num2 = (num2 << 5) + num2 + (num2 >> 27) ^ numPtr[1];
                    numPtr += 2;
                }
                if (length > 0)
                    num1 = (num1 << 5) + num1 + (num1 >> 27) ^ *numPtr;
                return num1 + num2 * 1566083941;
            }
        }
        
        #if UNITY_EDITOR
        [UnityEditor.MenuItem("Tools/DumpRumTimeTableString #v" )]
        public static void DumpRumTimeTableString()
        {
            System.Text.StringBuilder sb = new System.Text.StringBuilder();
            foreach (var pair in _strDictionary)
            { 
                sb.AppendLine($"{pair.Value}"); 
            } 
            System.IO.DirectoryInfo directory = new System.IO.DirectoryInfo(UnityEngine.Application.dataPath);
            if (directory.Exists && directory.Parent != null)
            {
                string runTimeLogPath = directory.Parent.FullName + "/RunTimeTableString.txt";
                System.IO.File.WriteAllText(runTimeLogPath, sb.ToString());
                UnityEditor.EditorUtility.OpenWithDefaultApp(runTimeLogPath); 
            } 
        }
        #endif
        
        
        
    }

}