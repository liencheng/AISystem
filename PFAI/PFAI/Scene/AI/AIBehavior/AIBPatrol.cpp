#include "AIBPatrol.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../AIBehavior/IBehavior.h"
#include "../AICondition/IAICon.h"
#include "../AIPolicy/IAIPolicy.h"
#include "../../Obj/Obj_Char.h"

void AIBPatrol::OnStart()
{
	IBehavior::OnStart();
}

void AIBPatrol::OnUpdate()
{
    IBehavior::OnUpdate();

    if(TimeOut())
    {
        OnEnd(E_AIBehaviorStatus::ABS_TimeOut);
    }
    // Perform patrol logic
    switch (m_pType)
    {
    case PatrolType::SearchEnemy:
        SearchEnemy();
        break;
    case PatrolType::SearchFriend:
        SearchFriend();
        break;
    case PatrolType::SearchPoint:
        SearchPoint();
        break;
    case PatrolType::SearchRange:
        SearchRange();
        break;
    }
}

void AIBPatrol::OnEnd(E_AIBehaviorStatus result)
{
    SetBehaviorStatus(E_AIBehaviorStatus::ABS_End);
}

bool AIBPatrol::Interrupt()
{
    OnEnd(E_AIBehaviorStatus::ABS_End);
    return true;
}

void AIBPatrol::SearchEnemy()
{
    /*
     *Scan the area for enemies
     *选择一个仇人
     *执行：追踪仇人
     *结束：超时&仇人死亡&追到可攻击范围之内
     */
}

void AIBPatrol::SearchPoint()
{
    /*
     *从多个点中随机一个 一直执行MoveTo
     *结束：超时&到达指定点
     */
}

void AIBPatrol::SearchFriend()
{
    /*
     *Scan the area for friends
     *选择一个仇人
     *执行：追踪仇人
     *结束：超时&仇人死亡&追到可攻击范围之内
     */
}

void AIBPatrol::SearchRange()
{
    /*
     *基于当前点和半径范围内的点
     *结束：超时&到达指定点
     */
}


