#pragma once

class AIDefine
{
public:
};
enum class E_AIPolicyType
{
        AIPolicyType_None = 0,
        AIPolicyType_Boss,
        AIPolicyType_NPC,
        AIPolicyType_Enemy,
        AIPolicyType_MAX
};

enum class E_AIBehaviorStatus
{
        ABS_Ready,
        ABS_Running,
        /*
         *ABS_Succ，ABS_Fail一定要在ABS_End之后，用于枚举值判断>=ABS_End时，整个行为的结果
         */
        ABS_End,
        ABS_Succ,
        ABS_Fail,
        ABS_TimeOut,
};


enum class E_AIGoalType
{
    G_None = 0,
    G_MoveTo,
    G_Chat,
    G_Attack,
    G_Follow,
};

