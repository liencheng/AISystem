
#include <iostream>
#include "Public.h"
#include "Editor/EDScene.h"
#include "Utils/Logger.h"
#include <thread> // Include this header for std::this_thread::sleep_for
#include <chrono> // Include this header for std::chrono::milliseconds
#include "Editor.h"




#ifndef MYDLL_EXPORT

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
	Editor::getInstance().LoadTable();
    //##################################################################################################
	Editor::getInstance().Init();
    int64_t totalTime = 0;
    while (true)
    {
        Editor::getInstance().Update(0.030f);
        std::this_thread::sleep_for(std::chrono::milliseconds(30)); // Replace time.Sleep with this
        totalTime += 30;
		std::string timeStr = std::to_string(totalTime);
        //LOG_INFO("aisystem run totalTime:" + timeStr);
    }
    //#################################################################################################
    return 0;

}
#endif // 
