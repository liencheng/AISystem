#pragma once
#include <vector>

#include "../AIBehavior/IBehavior.h"
#include "../AIKnowledge/AIKnowledge.h"
#include "../GameDfine_AI/AIDefine.h"

/*
 *IPolicy, AI策略接口
 *
 *心跳逻辑：驱动AI行为，用于根据AIKnowledge的状态来决定AI的行为
 *行为选择基于：已有的权重 和条件
 */
class IAIPolicy
{
public:
 IAIPolicy() = default;
protected:
 AIKnowledge * m_pAIKnowledge;
 AIPolicyType m_ePolicyType = AIPolicyType::AIPolicyType_None;
 std::vector<IBehavior *> m_vecBehavior;
 IBehavior * m_pCurrentBehavior = nullptr;
 
public:
 /*
  *AI心跳
  */
 virtual void Update(float fDeltaTime) = 0;

 /*
  *添加行为
  */
 virtual bool AddBehavior(IBehavior * pBehavior) = 0;

 /*
  *决策
  */
 virtual IBehavior* Decision() = 0;

 /*
  *获取当前行为
  */
 virtual IBehavior * SelectBestBehavior() const = 0 ; 
};
