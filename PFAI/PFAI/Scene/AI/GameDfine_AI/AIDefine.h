#pragma once

class AIDefine
{
public:
};
enum class AIPolicyType
{
        AIPolicyType_None = 0,
        AIPolicyType_Boss,
        AIPolicyType_NPC,
        AIPolicyType_Enemy,
        AIPolicyType_MAX
};

enum class AIBehaviorStatus
{
        ABS_None = 0,
        ABS_Ready,
        ABS_Running,
        ABS_End,
};

