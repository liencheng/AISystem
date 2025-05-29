#include "Obj_Char.h"



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

void Obj_Char::Update()
{
    pAI->Update(0);
}

