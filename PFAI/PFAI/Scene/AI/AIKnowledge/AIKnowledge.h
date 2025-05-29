#pragma once
#include <vector>
#include "../../../Routine/Scene.h"
#include "../../Obj/Obj_Char.h"
#include "../AIGoalSensor/IGoal.h"
#include "../AISignal/AISignal.h"
/*
 *AIKnowledge, AI知识库
 *Goals: 不直接与AI行为交互, 只提供数据
 *Signals: 事件，用于通知AI行为，如：打断，切换状态等, 优先级高于Goals，及Behaviour自身配置单额权重
 *pScene: 场景指针，用于获取场景中的对象
 *pPlayer: 玩家指针，用于获取玩家的信息
 */

class AIKnowledge
{
public:

private:
 Scene *            m_pScene = nullptr;
 Obj_Char *         m_pPlayer = nullptr;

 /*
 *AI目标列表，用于存储AI的目标信息
 *allow designer to add or remove goals dynamically
 *example:
    in some AI, we need to add a goal to occupy a certain position
 */
 std::vector<IGoal*> m_vecGoals;
 /*
    *AI事件列表，用于存储AI的事件信息
    *Signal: 信号，用于通知AI行为,收到信号之后，需要强制执行某些行为
 */
std::vector<AISignal> m_vecSignals;


public:
 AIKnowledge(Scene *pScene, Obj_Char *pPlayer);
 ~AIKnowledge();

 Obj_Char * GetPlayer() const{ return m_pPlayer; }

public:
 void Update();
 bool AddGoals(IGoal *pGoal);
 bool ReceiveSignal(const AISignal &signal);
 
private:
 void UpdateGoals();
 void UpdateSignals();
 
};
