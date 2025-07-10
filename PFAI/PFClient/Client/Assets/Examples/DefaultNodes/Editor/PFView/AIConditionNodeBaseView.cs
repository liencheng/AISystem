using System.Collections;
using System.Collections.Generic;
using GraphProcessor;
using UnityEngine.UIElements;

[NodeCustomEditor(typeof(AIConditionNodeBase))]
public class AIConditionNodeBaseView : BaseNodeView
{
	
	public AIConditionNodeBase node => nodeTarget as AIConditionNodeBase;
	public int TabId => node.ConditionId;

	public override void Enable()
	{
		/*
		public string ConditionDescription = "DefaultConditionDescription";
		public int ConditionId = 0;
		public string ConditionName = "DefaultCondition";
		public int ConditionPriority = 0;
		public int ConditionInterval = 0;
		public int ConditionTimeOut = 0;
		public int ConditionCD = 0;
		*/
		
		var node = nodeTarget as AIConditionNodeBase;
		var txtConditionId = new TextField("Condition Id") {
			value = node.ConditionId.ToString(),
		};
		txtConditionId.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIConditionNodeBase ConditionId");
				node.ConditionId = int.Parse(v.newValue);
			}
		);
		var txtConditionName = new TextField("Condition Name") {
			value = node.ConditionName,
		};
		txtConditionName.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIConditionNodeBase ConditionName");
				node.ConditionName = v.newValue;
			}
		);
		var txtConditionDescription = new TextField("Condition Description") {
			value = node.ConditionDescription,
		};
		txtConditionDescription.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIConditionNodeBase ConditionDescription");
				node.ConditionDescription = v.newValue;
			}
		);
		var foldout = new Foldout() { text = "固定参数" };
		foldout.Add(new Label("This is a ai condition node"));
		foldout.Add(new Label("You can desc ai condition here"));
		foldout.Add(txtConditionId);
		foldout.Add(txtConditionName);
		foldout.Add(txtConditionDescription);
		controlsContainer.Add(foldout);
	}
}
