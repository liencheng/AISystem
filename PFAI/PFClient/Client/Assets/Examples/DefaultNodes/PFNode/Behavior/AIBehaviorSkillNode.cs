using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Games.Table;
using GraphProcessor;

[System.Serializable, NodeMenuItem("PFAI/Behaviror/SkillNode")]
public class AIBehaviorSkillNode : AIBehaviorNodeBase
{
 #region Parameters
    public override string name => "AI Behavior Skill Node";

    public enum ParamsIndex
    {
        SkillId = 0,
    }
    
    public int SkillId = 0;
    
    public override void LoadParameters(int tabId)
    {
        Tab_NpcAIBehavior b = TableManager.GetNpcAIBehaviorByID(tabId);
        if (b.IsNull())
        {
            Debug.LogError($"AIBehaviorSkillNode LoadParameters: Tab_NpcAIBehavior with ID {tabId} not found.");
            return;
        }
        SkillId = b.GetParambyIndex((int)ParamsIndex.SkillId);
    }

    public override void Execute()
    {
        if (SkillId <= 0)
        {
            Debug.LogError("AIBehaviorSkillNode Execute: SkillId is not set or invalid.");
            return;
        }
        // Here you would implement the logic to execute the skill.
        Debug.Log($"Executing skill with ID: {SkillId}");
    }

    #endregion
}
