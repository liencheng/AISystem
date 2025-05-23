#include "IGoal.h"


void IGoal::OnUpdate(const AIKnowledge* pknowledge)
{
    if(IsSatisfyCon(pknowledge))
    {
        
    }
}


bool IGoal::IsSatisfyCon(const AIKnowledge* pK) const
{
    for (auto con : m_vecConditions)
    {
        if (!con->IsSatisfy(pK->m_pPlayer))
        {
            return false;
        }
    }
    return true;
}