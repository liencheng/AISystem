using System.Collections.Generic;
using UnityEngine;
using GraphProcessor;

[System.Serializable, NodeMenuItem("PFAI/AIRootNode")]
public class AIRootNode : BaseNode
{
	
	[Input("Parent", allowMultiple = true)]
	public int input;
	
    [Output("Children"), Multiline]
	public int	output;
	

	public override string name => "your ai name";

    public override bool isRenamable => true;

    protected override void Process()
    {
    }
    #region Custom Variables
    public string NpcName = "DefaultAI";
    public int PolicyId = -1;
    #endregion
    
}


