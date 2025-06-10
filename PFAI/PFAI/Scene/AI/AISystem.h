#pragma once
#include "AIKnowledge/AIKnowledge.h"
#include "AIPolicy/IAIPolicy.h"

class AISystem
{

public:
    AISystem(/* args */);
    ~AISystem();

private:
    /* data */
    AIKnowledge m_aiKnowledge;
    IAIPolicy   *m_aiPolicy;
};

