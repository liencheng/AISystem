#pragma once
#include <vector>

#include "../AIBehavior/IBehavior.h"
#include "../AIKnowledge/AIKnowledge.h"
#include "../GameDfine_AI/AIDefine.h"
#include "../../Obj/Obj_Char.h"

/*
 *IPolicy, AI策略接口
 *
 *心跳逻辑：驱动AI行为，用于根据AIKnowledge的状态来决定AI的行为
 *行为选择基于：已有的权重 和条件
 */
class IAIPolicy
{
public:
	IAIPolicy(const Obj_Char* pOwner) :m_pOwner(pOwner) {};
protected:
	AIKnowledge* m_pAIKnowledge;
	std::vector<IBehavior*> m_vecBehavior;
	std::vector<IDbgNess* > m_vecDbgNodes; // 调试节点
	IBehavior* m_pCurrentBehavior = nullptr;
	E_AIPolicyType m_ePolicyType = E_AIPolicyType::AIPolicyType_None;
	bool       m_bBehaviorDirty = false; // 行为是否改变
	const Obj_Char* m_pOwner = nullptr; // AI策略的拥有者，通常是一个角色对象

public:
	virtual void        Update(float fDeltaTime);
	virtual void		 Init();
	virtual IBehavior* Decision() = 0;
	virtual IBehavior* SelectBestBehavior() const = 0;


 void                UpdateView();
 void                UpdateDbg();
 
 bool        AddBehavior(IBehavior* pBehavior);
 bool        DelBehavior(IBehavior* pBehavior);

 void        MarkBehaviorDirty() { m_bBehaviorDirty = true; }
 void        ClearBehaviorDirty() { m_bBehaviorDirty = false; }
 bool        IsBehaviorDirty() const { return m_bBehaviorDirty; }
 
 AIKnowledge*        GetAIKnowledge()const { return m_pAIKnowledge; }        
 IDbgNess*           GetDbgNode(int32_t id) const;
 const Obj_Char* GetOwner() const { return m_pOwner; }

private:
 bool       AddDbgNode(IDbgNess* pDbgNode);
 bool       DelDbgNode(IDbgNess* pDbgNode);

};
