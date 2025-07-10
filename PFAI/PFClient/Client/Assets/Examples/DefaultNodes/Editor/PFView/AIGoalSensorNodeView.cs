using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEditor.UIElements;
using UnityEditor.Experimental.GraphView;
using UnityEngine.UIElements;
using GraphProcessor;
using System.Linq;
using NUnit.Framework;
using UnityEditor.Search;

[NodeCustomEditor(typeof(AISensorNode))]
public class AISensorNodeView : BaseNodeView
{
	public override void Enable()
	{
		var node = nodeTarget as AISensorNode;

		List<SensorType> sensorTypes = Enum.GetValues(typeof(SensorType)).Cast<SensorType>().ToList();

		var popupmenu = new PopupField<SensorType>(
			"Sensor Type",
			sensorTypes,
			SensorType.Chat,
			sensorType => sensorType.ToString(),
			sensorType => sensorType.ToString()
		);


		var golaSensorName = new TextField("Goal Sensor Name");
		golaSensorName.value = node.GoalSensorName;
		golaSensorName.RegisterValueChangedCallback(
			v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AISensorNode GoalSensorName");
				node.GoalSensorName = v.newValue;
			}
		);

		var p = new IntegerField("Prority") { value = node.Prority };
		var t = new IntegerField("Timeout") { value = node.GoalTimeOut };
		var i = new IntegerField("Interval") { value = node.CalGoalInterval };
		var button = new Button(() =>
		{
			owner.RegisterCompleteObjectUndo("Updated AISensorNode SensorType");
			node.SensorType = (SensorType)EditorUtility.DisplayDialogComplex("Select Sensor Type",
				"Choose the type of sensor", "Chat", "Combat", "Escape");
		})
		{
			text = "Change Sensor Type"
		};

		var toggle = new Toggle("Debug")
		{
			value = node.debug,
			tooltip = "Enable or disable debug mode for this sensor node."
		};
		toggle.RegisterValueChangedCallback(v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AISensorNode Debug");
				node.debug = toggle.value;
				SetNodeColor(node.debug ? Color.red : Color.green);
			}
		);


		p.RegisterValueChangedCallback(v =>
		{
			owner.RegisterCompleteObjectUndo("Updated AISensorNode Prority");
			node.Prority = v.newValue;
		});
		t.RegisterValueChangedCallback(v =>
			{
				owner.RegisterCompleteObjectUndo("Updated AISensorNode GoalTimeOut");
				node.GoalTimeOut = v.newValue;
			}
		);
		i.RegisterValueChangedCallback(v =>
		{
			owner.RegisterCompleteObjectUndo("Updated AISensorNode CalGoalInterval");
			node.CalGoalInterval = v.newValue;
		});

		controlsContainer.Add(golaSensorName);
		controlsContainer.Add(p);
		controlsContainer.Add(t);
		controlsContainer.Add(i);
		controlsContainer.Add(popupmenu);
		controlsContainer.Add(button);
		topPortContainer.Add(toggle);
	}
}
