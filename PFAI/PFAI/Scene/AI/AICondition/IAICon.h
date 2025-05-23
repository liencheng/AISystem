#pragma once

class Obj_Char;

class IAICon
{
public:
    virtual bool IsSatisfy(Obj_Char * pOwner) = 0; // Called to check the condition
};
