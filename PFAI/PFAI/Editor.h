#pragma once
#include "Public.h"
#include "Editor/EDScene.h"

class Editor
{

public:
    static Editor& getInstance()
    {
        static Editor instance;
        return instance;
    }
private:
    Editor() {};
    ~Editor() {}
public:
    Editor(const Editor&) = delete;
    Editor operator = (const Editor&) = delete;
    //Editor& operate = (const Editor&);

    void Init()
    {
        m_Scene.Init();
    }
    void Update(float deltaTime)
    {
        m_Scene.Update(deltaTime);
    }
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
private:
    EDScene m_Scene;
};

