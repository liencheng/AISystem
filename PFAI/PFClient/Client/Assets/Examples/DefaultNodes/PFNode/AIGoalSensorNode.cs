using UnityEngine;
using GraphProcessor;
using Games.Table;

[System.Serializable]
public enum SensorType
{
	Chat, 
	Combat, 
	Escape
}
[System.Serializable, NodeMenuItem("PFAI/AIGoalSensorNode")]
public class AISensorNode : BaseNode
{
    [Output("Out")]
	public int		output;
	
    [Input("In", allowMultiple = true)]
	public int	input;

	public override string name => "GoalSensor";

    public override bool isRenamable => true;

	protected override void Process() => output = input;
	
	#region Custom
	public	void Init(int nSensorTabId)
	{
		Tab_NpcAIGoalSensor tabSensor = TableManager.GetNpcAIGoalSensorByID(nSensorTabId);
		if (tabSensor.IsNull())
		{
			Debug.LogError($"Init AISensorNode Error: Sensor not found for ID: {nSensorTabId}");
			return;
		}
		GoalSensorId = nSensorTabId;
		GoalSensorName = tabSensor.Name;
		SensorType = (SensorType)tabSensor.Type;
		Prority = tabSensor.Prority;
		CalGoalInterval = tabSensor.CalGoalInterval;
		GoalTimeOut = tabSensor.GoalTimeOut;
	}
	
	public SensorType SensorType = SensorType.Chat;
	public int GoalSensorId = 0;
	public string GoalSensorName = "DefaultGoalSensor";
	public int Prority = 0;
	public int CalGoalInterval = 0;
	public int GoalTimeOut = 0;
	#endregion
	
}