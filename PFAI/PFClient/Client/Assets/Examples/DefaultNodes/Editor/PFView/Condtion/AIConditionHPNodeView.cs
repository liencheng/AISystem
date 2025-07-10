using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine.UIElements;

[NodeCustomEditor(typeof(AIConditionHPNode))]
public class AIConditionHPNodeView : AIConditionNodeBaseView
{
    public override void Enable()
    {
        base.Enable();
        // Additional initialization if needed
      
        
        /*
    public ConditionType conditionType = ConditionType.EqualTo;
    public int HP = 0;
    */
        var node = nodeTarget as AIConditionHPNode;
        var txtConditionType = new EnumField("Condition Type", node.conditionType);
        txtConditionType.RegisterValueChangedCallback(
            v =>
            {
                owner.RegisterCompleteObjectUndo("Updated AIConditionHPNode ConditionType");
                node.conditionType = (AIConditionHPNode.ConditionType)v.newValue;
            }
        );
        mainContainer.Add(txtConditionType);
        var txtHP = new IntegerField("HP") {
            value = node.HP,
        };
        txtHP.RegisterValueChangedCallback(
            v =>
            {
                owner.RegisterCompleteObjectUndo("Updated AIConditionHPNode HP");
                node.HP = v.newValue;
            }
        );
        mainContainer.Add(txtHP);
        
    }
}
