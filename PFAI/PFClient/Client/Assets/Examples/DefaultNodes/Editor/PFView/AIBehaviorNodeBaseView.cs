using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine.UIElements;

[NodeCustomEditor(typeof(AIBehaviorNodeBase))]
public class AIBehaviorNodeBaseView : BaseNodeView
{
	
	public AIBehaviorNodeBase node => nodeTarget as AIBehaviorNodeBase;
	public int TabId => node.BehaviorId;
	
	public override void Enable()
	{
		var node = nodeTarget as AIBehaviorNodeBase;
		
	/*
	public int BehaviorId = 0;
	public string BehaviorName = "DefaultBehavior";
	public int BehaviorPriority = 0;
	public int BehaviorInterval = 0;
	public int BehaviorTimeOut = 0;
	*/
	var txtBehaviorId = new TextField("Behavior Id") {
			value = node.BehaviorId.ToString(),
		};
		txtBehaviorId.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIBehaviorNodeBase BehaviorId");
				node.BehaviorId = int.Parse(v.newValue);
			}
		);
		
		var txtBehaviorName = new TextField("Behavior Name") {
			value = node.BehaviorName,
		};
		txtBehaviorName.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIBehaviorNodeBase BehaviorName");
				node.BehaviorName = v.newValue;
			}
		);
		
		var txtBehaviorPriority = new TextField("Behavior Priority") {
			value = node.BehaviorPriority.ToString(),
		};
		txtBehaviorPriority.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIBehaviorNodeBase BehaviorPriority");
				node.BehaviorPriority = int.Parse(v.newValue);
			}
		);
		
		var behaviorCD = new TextField("Behavior CD") {
			value = node.BehaviorCD.ToString(),
		};
		 behaviorCD.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIBehaviorNodeBase BehaviorCD");
				node.BehaviorCD = int.Parse(v.newValue);
			}
		);
		
		var txtBehaviorTimeOut = new TextField("Behavior TimeOut") {
			value = node.BehaviorTimeOut.ToString(),
		};
		
		txtBehaviorTimeOut.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIBehaviorNodeBase BehaviorTimeOut");
				node.BehaviorTimeOut = int.Parse(v.newValue);
			}
			
		);
		controlsContainer.Add(txtBehaviorId);
		controlsContainer.Add(txtBehaviorName);
		controlsContainer.Add(txtBehaviorPriority);
		controlsContainer.Add( behaviorCD);
		controlsContainer.Add(txtBehaviorTimeOut);
		
		
		//Button Trigger Execute()
		var btnExecute = new Button(() =>
		{
			owner.RegisterCompleteObjectUndo("Execute AIBehaviorNodeBase");
			node.Execute();
		})
		{
			text = "Execute",
			name = "Execute"
		};
		titleContainer.Add(btnExecute);
	}
	
}
