#pragma once
#include <cstdint>

#include "IBehavior.h"
#include "../../../Public/DataDefine.h"
#include "../../Obj/Obj_Char.h"

/*详情介绍：
 *巡逻逻辑
 *设计目的：寻找周围目标
 *是否可以打断：可以打断
 *优先级：较低
 */
enum class PatrolType
{
    SearchRange = 0, // 最大范围巡逻
    SearchPoint = 1, // 指定点巡逻
    SearchEnemy = 2, // 搜索敌人
    SearchFriend = 3, // 搜索友方
};

class AIBPatrol:IBehavior
{
public:
    AIBPatrol(Obj_Char *owner):IBehavior(owner){}
    ~AIBPatrol() = default;

    void OnStart() override;
    void OnUpdate() override;
    void OnEnd() override;
    bool Interrupt() override;

private:
    void SearchEnemy(); // Search for enemies
    void SearchFriend(); // Search for friends
    void SearchPoint(); // Search for a specific point
    void SearchRange(); // Search within a range

private:
    ScenePos        m_vecPatrolPoints[5]; // Array of patrol points
    int32_t         m_nPatrolPointIndex = 0; // Index of the patrol point
    bool            m_bIsPatrolling = false; // Flag indicating if the character is patrolling
    PatrolType      m_pType = PatrolType::SearchRange; // Type of patrol
};
