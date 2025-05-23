#pragma once

class IGoal
{
public:
    virtual void OnStart() = 0; // Called when the goal starts
    virtual void OnUpdate() = 0; // Called every frame while the goal is active
    virtual void OnEnd() = 0; // Called when the goal ends
};
