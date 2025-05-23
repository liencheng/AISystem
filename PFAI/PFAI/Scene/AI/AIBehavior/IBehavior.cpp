#include "IBehavior.h"


bool IBehavior::IsSatisfyCondition()
{
    for (auto condition : m_vecConditions)
    {
        if (!condition->IsSatisfy())
        {
            return false;
        }
    }
    return true;
}
