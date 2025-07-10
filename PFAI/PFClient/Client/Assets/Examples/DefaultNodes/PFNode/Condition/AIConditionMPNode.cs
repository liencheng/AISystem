using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using GraphProcessor;
using Games.Table;

[System.Serializable, NodeMenuItem("PFAI/Condtion/HPNode")]
public class AIConditionMPNode : AIConditionNodeBase
{
    public enum ConditionType
    {
        GreaterThan,
        LessThan,
        EqualTo
    }
    #region MyRegion
    
    public override void LoadParameters(int tabId)
    {
        Tab_NpcAICondition condition = TableManager.GetNpcAIConditionByID(tabId);
        if (condition.IsNull())
        {
            Debug.LogError($"AIConditionMPNode LoadParameters: Tab_NpcAICondition with ID {tabId} not found.");
            return;
        }
        conditionType = (ConditionType)condition.GetParambyIndex(0); // Assuming index 0 is for condition type
        MP = condition.GetParambyIndex(1); // Assuming index 1 is for MP value
    }
    public ConditionType conditionType = ConditionType.EqualTo;
    public int MP = 0;
    #endregion
}
