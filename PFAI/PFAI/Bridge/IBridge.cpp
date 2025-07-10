#include "Public.h"
#include "IBridge.h"
#include "../Editor.h"

void __cdecl CPPBridge_Init()
{
    //##################################################################################################
    utils::Logger::getInstance().setLogFile("log.txt");
    //##################################################################################################

    //##################################################################################################
    //LOG_INFO("Start UP!");
    //##################################################################################################

    //##################################################################################################
    //LOG_INFO("Load Table!");
	Editor::getInstance().LoadTable();
	Editor::getInstance().Init();
}

void __cdecl CPPBridge_Update(float deltaTime)
{
	Editor::getInstance().Update(deltaTime);
}

const void __cdecl CPPBridge_GetGoalSensor(BridgeGoalSensor* sensor)
{
    //LOG_INFO("CPPBrige_GetGoalSensor Start");
    sensor->Id = 10000;
    for (int idx = 0; idx < 10; idx++)
    {
        sensor->conList[idx].Id = idx;
        sensor->conList[idx].Result = idx / 2 == 0;
    }
    //LOG_INFO("CPPBrige_GetGoalSensor End");
}

