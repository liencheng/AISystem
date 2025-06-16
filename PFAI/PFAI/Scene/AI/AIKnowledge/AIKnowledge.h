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
   AIKnowledge(Obj_Char *pChar):m_pOwner(pChar) {
      InitGoals();
      m_pScene = m_pOwner->GetScene();
   };
   ~AIKnowledge(){}
   void InitGoals();

private:
   Scene *            m_pScene = nullptr;
   Obj_Char *         m_pOwner = nullptr;
   std::vector<IGoal>     m_vecGoals;
   std::vector<AISignal>   m_vecSignals;

   bool              m_bDirty;

public:
   Obj_Char *  GetPlayer() const{ return m_pOwner; }
   Scene *     GetScene() const{ return m_pScene; }
 void Update();

 bool AddGoals(IGoal &pGoal);
 bool DelGoals(IGoal &pGoal);

 bool ProduceSignal(const AISignal &signal);
 bool ConsumeSignal(const AISignal &signal);

 void MarkDirty() { m_bDirty = true;}
 void ClearDirty() { m_bDirty = false;}
 bool IsDirty() {return m_bDirty;}
 
private:
 void UpdateGoals();
 void UpdateSignals();
}; 
