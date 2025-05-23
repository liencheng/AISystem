#pragma once
#include <algorithm>
#include <cstdint>
#include <iostream>

#include "../../Public/DataDefine.h"

class Obj_Char
{
public:
    // Constructor
    Obj_Char();
    // Destructor
    ~Obj_Char();
    // Initialize the object
    void Init();
    // Update the object
    void Update();
    // Render the object
    void Render();
    void Caskill(int32_t skillId){ std::cout<<"Cast skill: " << skillId << std::endl; }
    void MoveTo(ScenePos pos){ std::cout<<"Move to: " << pos.x << ", " << pos.y << ", " << pos.z << std::endl; }
};
