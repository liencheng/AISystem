using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;


[StructLayout(LayoutKind.Sequential)]
public struct BridgeCondition
{
    public int Id;
    public bool Result;
}

[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
public struct BridgeGoalSensor
{
    public int Id;
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]   
    public BridgeCondition[] Conditions;
}

public class CPPBridge
{
    // Importing C++ functions
    [DllImport("PFAI", CallingConvention = CallingConvention.Cdecl)]
    static extern public void CPPBridge_Init();

    [DllImport("PFAI", CallingConvention = CallingConvention.Cdecl)]
    static extern public void CPPBridge_Update();

    [DllImport("PFAI", CallingConvention = CallingConvention.Cdecl)]
    static extern public void CPPBridge_Stop();

    [DllImport("PFAI", CallingConvention = CallingConvention.Cdecl)]
    static extern public void CPPBridge_GetGoalSensor(out BridgeGoalSensor goalSensor);
    
    public void CPPBridge_AddCondition()
    {
        Debug.Log("CPPBridge SampleTo");
    }
}
