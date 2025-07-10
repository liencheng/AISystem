using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine;
using Games.Table;

[System.Serializable, NodeMenuItem("PFAI/Behaviror/ChatNode")]
 public class AIBehaviorChatNode : AIBehaviorNodeBase
{
    public override string name => "AI Behavior Chat Node";
    
    public enum ParamsIndex
    {
        ChatId = 0,
    }
    
    public override void LoadParameters(int tabId)
    {
        Tab_NpcAIBehavior tab = TableManager.GetNpcAIBehaviorByID(tabId);
        ChatId = tab.GetParambyIndex((int)ParamsIndex.ChatId);
    }

    public override void Execute()
    {
        if (ChatId <= 0)
        {
            Debug.LogError("AIBehaviorChat Execute: ChatId is not set or invalid.");
            return;
        }
        // Here you would implement the logic to execute the chat.
        Debug.Log($"Executing chat with ID: {ChatId}");
    }

    #region Custom Variables
    public int ChatId;
    #endregion
}
