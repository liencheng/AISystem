using System.Collections;
using System.Collections.Generic;
using UnityEngine.UIElements;
using Games.Table;
using GraphProcessor;

[NodeCustomEditor(typeof(AIBehaviorSkillNode))]
public class AIBehaviorSkillNodeView : AIBehaviorNodeBaseView
{
    public override void Enable()
    {
        base.Enable();
        
		var node = nodeTarget as AIBehaviorSkillNode;
        //SkillId 
        if (node == null)
        {
            return;
        }
        var skillIdField = new IntegerField("Skill Id")
        {
            value = node.SkillId,
            name = "skillId"
        };
        skillIdField.RegisterValueChangedCallback(evt =>
        {
            owner.RegisterCompleteObjectUndo("Updated AIBehaviorSkillNode SkillId");
            node.SkillId = evt.newValue;
        });
        mainContainer.Add(skillIdField);
    }
    
    
    
}
