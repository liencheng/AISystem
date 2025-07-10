using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Utils 
{
    public static void CreateTableTextAsset(string assetPath, byte[] bytes)
    {
#if UNITY_EDITOR 
        try
        {  
            System.IO.File.WriteAllBytes(assetPath,bytes);
            Debug.Log($"SaveBinarySheet => {assetPath}");
        }
        catch (System.Exception e)
        { 
            Debug.LogError($"Serialize Table {assetPath}  Error : {e.Message} {e.StackTrace}");
        }
#endif 
    }
}
