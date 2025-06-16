#pragma once
#include <algorithm>
#include <cstdint>
#include <iostream>

#include "../../Public/DataDefine.h"
#include "../AI/AIPolicy/IAIPolicy.h"

class Obj_Char
{

private:
    IAIPolicy * pAI;
    Scene * pScene;

public:
    // Constructor
    Obj_Char();
    // Destructor
    ~Obj_Char();
    // Initialize the object
    void Init();
    // Update the object
    void Update(float deltaTime);
    // Render the object
    void Render();
    void Caskill(int32_t skillId){ std::cout<<"Cast skill: " << skillId << std::endl; }
    void MoveTo(ScenePos pos){ std::cout<<"Move to: " << pos.x << ", " << pos.y << ", " << pos.z << std::endl; }
    int64_t GetHP()const{ return  0;}
    int64_t GetMP()const{ return  0;}
    bool IsInCombat()const {return  false;}
    Scene * GetScene()const{ return  pScene;}
    int64_t GetDataID() const { return 0; } // TODO: 实现获取角色DataID的逻辑
};
