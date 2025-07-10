using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine.UIElements;

[NodeCustomEditor(typeof(AIBehaviorChatNode))]
public class AIBehaviorChatNodeView : AIBehaviorNodeBaseView
{
    public override void Enable()
    {
        base.Enable();
        
        var node = nodeTarget as AIBehaviorChatNode;
        if (node == null)
        {
            return;
        }
        
        // ChatId
        var chatIdField = new IntegerField("Chat Id")
        {
            value = node.ChatId,
            name = "chatId"
        };
        chatIdField.RegisterValueChangedCallback(evt =>
        {
            owner.RegisterCompleteObjectUndo("Updated AIBehaviorChatNode ChatId");
            node.ChatId = evt.newValue;
        });
        mainContainer.Add(chatIdField);
    }
}
