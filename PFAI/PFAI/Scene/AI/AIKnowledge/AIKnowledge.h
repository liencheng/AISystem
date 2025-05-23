#pragma once
#include <vector>
#include "../../../Routine/Scene.h"
#include "../../Obj/Obj_Char.h"
#include "../AIGoalSensor/IGoal.h"
/*
 *AIKnowledge, AI知识库
 *Goals: 不直接与AI行为交互, 只提供数据
 *Enents: 事件，用于通知AI行为，如：打断，切换状态等
 *pScene: 场景指针，用于获取场景中的对象
 *pPlayer: 玩家指针，用于获取玩家的信息
 */

class AIKnowledge
{
public:
 Scene * m_pScene = nullptr;
 Obj_Char * m_pPlayer = nullptr;
 std::vector<IGoal *> m_vecGoals;

private:
 void UpdateGoals(){}
};
