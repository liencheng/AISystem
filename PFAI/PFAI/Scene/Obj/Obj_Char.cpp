#include "Public.h"
#include "Obj_Char.h"
#include "../AI/AIPolicy/AIBossPolicy.h"
#include "../AI/AIPolicy/IAIPolicy.h"

Obj_Char::Obj_Char()
{
    pAI = nullptr;
}
Obj_Char::~Obj_Char()
{
    if (pAI != nullptr)
    {
        delete pAI;
        pAI = nullptr;
    }
}


void Obj_Char::Init()
{
	pAI = new AIBossPolicy(this); // Assuming IAIPolicy has a default constructor
	if (pAI)
	{
		pAI->Update(0); // Initialize AI policy
	}
	else
	{
		LOG_ERROR("Failed to create IAIPolicy instance.");
	}
}

void Obj_Char::Update(float deltatime)
{
    pAI->Update(deltatime);
}

