using UnityEngine;
using GraphProcessor;
using Games.Table;
using UnityEngine.Serialization;

[System.Serializable, NodeMenuItem("PFAI/Behaviror Node")]
public class AIBehaviorNodeBase : BaseNode
{
    [Output("Out")]
	public int	output;
	
    [Input("In", allowMultiple = true)]
	public int	input;

	public override string name => "Behavior Node";

    public override bool isRenamable => true;

    protected override void Process()
    {
	    Debug.LogError($"{name} Process called, BehaviorId: {BehaviorId}");
    }
    
    #region CustomFunc

    public void Init(int nBehaviroTabId)
    {
	    Tab_NpcAIBehavior tabBehavior = TableManager.GetNpcAIBehaviorByID(nBehaviroTabId);
	    if (tabBehavior.IsNull())
	    {
		    Debug.LogError($"Init AIBehaviorNodeBase Error: Behavior not found for ID: {nBehaviroTabId}");
		    return;
	    }

	    BehaviorId = nBehaviroTabId;
	    BehaviorName = "TodoBehavior: " + BehaviorId;
	    BehaviorPriority = tabBehavior.Proprity;
	    BehaviorCD = tabBehavior.CD;
	    BehaviorTimeOut = tabBehavior.Timeout;
	    
	    LoadParameters(nBehaviroTabId);

    }
    public virtual void LoadParameters(int tabId)
	{
		Debug.LogWarning("LoadParameters not implemented in " + this.GetType().Name);
	}

	public virtual void Execute()
	{
		Debug.LogWarning("Execute not implemented in " + this.GetType().Name);
	}
    
    #endregion
	
	#region Custom
	public int BehaviorId = 0;
	public string BehaviorName = "DefaultBehavior";
	public int BehaviorPriority = 0;
	public float BehaviorCD = 0;
	public int BehaviorTimeOut = 0;
	#endregion
}