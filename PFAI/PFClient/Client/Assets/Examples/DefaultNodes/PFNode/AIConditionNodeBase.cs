using UnityEngine;
using GraphProcessor;
using Games.Table;
[System.Serializable, NodeMenuItem("PFAI/CondtionNode")]
public class AIConditionNodeBase : BaseNode
{
    [Output("Out")]
	public int		output;
	
    [Input("In")]
	public int		input;

	public override string name => "Renamable";

    public override bool isRenamable => true;

	protected override void Process() => output = input;
	
    #region CustomFunc

    public void Init(int nConditionTabId)
    {
	    Tab_NpcAICondition tabCondition = TableManager.GetNpcAIConditionByID(nConditionTabId);
	    if (tabCondition.IsNull())
	    {
		    Debug.LogError($"Init AIConditionNodeBase Error: Condition not found for ID: {nConditionTabId}");
		    return;
	    }
	    ConditionId = nConditionTabId;
	    ConditionName = tabCondition.Name;
	    ConditionDescription = "todo: " + ConditionName;
	    LoadParameters(nConditionTabId);
    }

    public virtual void LoadParameters(int tabId)
	{
		Debug.LogWarning("LoadParameters not implemented in " + this.GetType().Name);
	}
    #endregion
	
	
	#region Custom Variables
	public int ConditionId = 0;
	public string ConditionName = "DefaultCondition";
	public string ConditionDescription = "DefaultConditionDescription";
	#endregion
}