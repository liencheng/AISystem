using UnityEngine;
using GraphProcessor;

public enum AIPolicyType
{
	None,
	Boss,
	Npc,
	Monster,
	Friend,
}
[System.Serializable, NodeMenuItem("PFAI/AIPolicy")]
public class AIBehaviorPolicy : BaseNode
{
	
	public AIPolicyType policyType = AIPolicyType.None;
	
    [Input("In")]
	public int input;
	
	[Input("Knowledge")]
	public int knowledge;
	[Output("Behavior")]
	public int behavior;

	public override string name
	{
		get
		{
			return "AIPolicy: " + policyType.ToString();
		}	
	}

    public override bool isRenamable => true;

	protected override void Process() 
	{
		
		// Example processing logic
		Debug.LogError("Processing AIBehaviorPolicy with type: " + policyType);
		// Do something with the input
	}


	#region Custom Variables
	public int PolicyId = 0;
	#endregion
}