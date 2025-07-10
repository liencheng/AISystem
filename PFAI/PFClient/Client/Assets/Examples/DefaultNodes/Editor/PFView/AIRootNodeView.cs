using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEditor.UIElements;
using UnityEditor.Experimental.GraphView;
using UnityEngine.UIElements;
using GraphProcessor;
using System.Linq;

[NodeCustomEditor(typeof(AIRootNode))]
public class AIRootNodeView : BaseNodeView
{
	public override void Enable()
	{
		var node = nodeTarget as AIRootNode;

		var lalPolicyIdDes = new Label("PolicyID:");
		var lblPolicyId = new Label("Policy Id");
		lblPolicyId.text = node.PolicyId.ToString();
		lblPolicyId.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIRootNode PolicyId");
				node.PolicyId = int.Parse(v.newValue);
			}
		);
		var charNameField = new TextField("Character Name") {
			value = node.NpcName,
		};		
		charNameField.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AIRootNode NpcName");
				node.NpcName = v.newValue;
			}
		);
		
		var foldout = new Foldout() { text = "String" };
		foldout.Add(new Label("This is a ai root node"));
		foldout.Add(new Label("You can desc ai logic here"));
		controlsContainer.Add(foldout); 
		titleContainer.Add(lalPolicyIdDes);
		titleContainer.Add(lblPolicyId);
		controlsContainer.Add(charNameField);
		
	}
}