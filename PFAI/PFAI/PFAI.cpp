
#include <iostream>
#include "Public.h"
#include "Editor/EDScene.h"
#include "Utils/Logger.h"
#include <thread> // Include this header for std::this_thread::sleep_for
#include <chrono> // Include this header for std::chrono::milliseconds

class Editor
{
public:
    Editor() {
    };
    ~Editor() {}

    void Init()
    {
        m_Scene.Init();
    }
    void Update(float deltaTime)
    {
        m_Scene.Update(deltaTime);
    }
private:
    EDScene m_Scene;
};

void LoadTable()
{
    LOG_INFO("Load Table!");
	TABLE_LOAD(Table_NpcAIBehavior);
	TABLE_LOAD(Table_NpcAICondition);
	TABLE_LOAD(Table_NpcAIGoalSensor);
	TABLE_LOAD(Table_NpcAIPolicy);
	TABLE_LOAD(Table_NpcAIPolicyRoot);
    LOG_INFO("Load Table Done!");
}

int main(int argc, char* argv[])
{
    //##################################################################################################
    utils::Logger::getInstance().setLogFile("log.txt");
    //##################################################################################################

    //##################################################################################################
    LOG_INFO("Start UP!");
    //##################################################################################################


    //##################################################################################################
    LOG_INFO("Load Table!");
	LoadTable();
    //##################################################################################################
    Editor editor;
	editor.Init();
    int64_t totalTime = 0;
    while (true)
    {
        editor.Update(0.030f);
        std::this_thread::sleep_for(std::chrono::milliseconds(30)); // Replace time.Sleep with this
        totalTime += 30;
		std::string timeStr = std::to_string(totalTime);
        LOG_INFO("aisystem run totalTime:" + timeStr);
    }
    //#################################################################################################
    return 0;
}
