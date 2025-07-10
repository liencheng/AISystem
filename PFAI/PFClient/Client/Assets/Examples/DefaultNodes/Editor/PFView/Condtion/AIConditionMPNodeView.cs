using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine;
using UnityEngine.UIElements;

[NodeCustomEditor(typeof(AIConditionMPNode))]
public class AIConditionMPNodeView : AIConditionNodeBaseView
{
    public override void Enable()
    {
        base.Enable();
        // Additional initialization if needed
      
        
        var node = nodeTarget as AIConditionMPNode;
        var txtConditionType = new EnumField("Condition Type", node.conditionType);
        txtConditionType.RegisterValueChangedCallback(
            v =>
            {
                owner.RegisterCompleteObjectUndo("Updated AIConditionHPNode ConditionType");
                node.conditionType = (AIConditionMPNode.ConditionType)v.newValue;
            }
        );
        mainContainer.Add(txtConditionType);
        var txtMP = new IntegerField("MP") {
            value = node.MP,
        };
        txtMP.RegisterValueChangedCallback(
            v =>
            {
                owner.RegisterCompleteObjectUndo("Updated AIConditionHPNode MP");
                node.MP = v.newValue;
            }
        );
        mainContainer.Add(txtMP);
        
    }
}
