#pragma once
#include <string>
#include <cstring>
#include "../Scene/AI/AIBehavior/AIBPatrol.h"
#include "../Scene/Obj/Obj_Char.h"


struct BridgeCondition
{

public:
    int Id;
    bool Result;
};

struct BridgeGoalSensor
{
public:
    int Id;
    BridgeCondition conList[10];
};


extern "C"
{

    __declspec(dllexport)
       void __cdecl  CPPBridge_Init();
    __declspec(dllexport)
        void __cdecl CPPBridge_Update(float deltaTime);
    __declspec(dllexport)
        const void __cdecl CPPBridge_GetGoalSensor(BridgeGoalSensor * sensor);
}