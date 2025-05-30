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
 std::vector<IBehavior*> m_vecBehavior;
 std::vector<IDbgNess* > m_vecDbgNodes; // 调试节点
 IBehavior * m_pCurrentBehavior = nullptr;
 E_AIPolicyType m_ePolicyType = E_AIPolicyType::AIPolicyType_None;
 
public:
 virtual void        Update(float fDeltaTime) = 0;
 virtual IBehavior*  Decision() = 0;
 virtual IBehavior*  SelectBestBehavior() const = 0 ;
 
 bool        AddBehavior(IBehavior* pBehavior);
 bool        DelBehavior(IBehavior* pBehavior);
 
 AIKnowledge*        GetAIKnowledge()const { return m_pAIKnowledge; }        
 IDbgNess*           GetDbgNode(int32_t id) const;
};
