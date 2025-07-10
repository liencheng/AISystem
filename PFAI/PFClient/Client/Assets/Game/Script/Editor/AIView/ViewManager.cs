using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using GraphProcessor;
using Games.Table;
using Unity.Mathematics;
using UnityEditor;
using Unity.Mathematics.Geometry;


public class ViewManager : BaseGraphWindow
{
	[MenuItem("Window/ViewManager")]
	public static BaseGraphWindow OpenWithTmpGraph()
	{
        int nRootId = 1;
        AIPolicy ai = new AIPolicy(nRootId);
        var graph = ScriptableObject.CreateInstance<PolicyGraph>();
		var graphWindow = CreateWindow< ViewManager>();
		// When the graph is opened from the window, we don't save the graph to disk
        graphWindow.policyGraph = graph;
		graphWindow.policyGraph.hideFlags = HideFlags.HideAndDontSave;
		graphWindow.InitializeGraph(graphWindow.policyGraph);

        BuildAIGraph.DoBuildAIGraph(graphWindow, ai, graph);
        
		graphWindow.Show();
        
        // Set the static instance to the current graph window, 这句代码稍稍有些奇怪了
        ViewManager.Instance = graphWindow;
        
		return graphWindow;
	}
    
    protected override void Update()
    {
        base.Update();
        // 这里可以添加一些更新逻辑
        int nRootId = 1;
    }

    public static ViewManager m_Instance;
    public static ViewManager Instance
    {
        get
        {
            if (m_Instance == null)
            {
                m_Instance = OpenWithTmpGraph() as ViewManager;
            }
            return m_Instance;
        }
        set { m_Instance = value; }
    }
    
    
	PolicyGraph	policyGraph = new PolicyGraph();
    // Start is called before the first frame update

	protected override void OnDestroy()
	{
		graphView?.Dispose();
		DestroyImmediate(policyGraph);
	}

	protected override void InitializeWindow(BaseGraph graph)
	{
		titleContent = new GUIContent("Default Graph");

		if (graphView == null)
			graphView = new BaseGraphView(this);

		rootView.Add(graphView);
	}
    
    public BaseNodeView AddNode(BaseNode node)
    {
        BaseNodeView view = graphView.AddNode(node);
        return view;
    }
    #region Data 
    private AIRootNodeView m_rootNodeView;
    private List<AIBehaviorNodeBaseView> m_behaviorNodeViews = new List<AIBehaviorNodeBaseView>();
    private List<AIConditionNodeBaseView> m_conditionNodes = new List<AIConditionNodeBaseView>();
    private List<AISensorNodeView> m_sensorNodes = new List<AISensorNodeView>();
    public string name => "PolicyGraph";
    #endregion
    
    public AIRootNodeView RootNodeView
    {
        get => m_rootNodeView;
        set
        {
            if (m_rootNodeView != value)
            {
                m_rootNodeView = value;
            }
        }
    }
    
    public AIBehaviorNodeBaseView AddBehaviorNodeView(AIBehaviorNodeBaseView behaviorNodeView)
    {
        if (behaviorNodeView == null)
            return null;
        m_behaviorNodeViews.Add(behaviorNodeView);
        return behaviorNodeView;
    }
    
    public AIBehaviorNodeBaseView FindBehaviorNodeViews(int tabId)
    {
        return m_behaviorNodeViews.Find(b=> b.TabId == tabId);
    }
    
    public AIConditionNodeBaseView AddConditionNodeView(AIConditionNodeBaseView conditionNodeView)
    {
        if (conditionNodeView == null)
            return null;
        m_conditionNodes.Add(conditionNodeView);
        return conditionNodeView;
    }
    
    public AIConditionNodeBaseView FindConditionNodeView(int tabId)
    {
        return m_conditionNodes.Find(c => c.TabId == tabId);
    }
    
    public AISensorNodeView AddSensorNodeView(AISensorNodeView sensorNodeView)
    {
        if (sensorNodeView == null)
            return null;
        m_sensorNodes.Add(sensorNodeView);
        return sensorNodeView;
    }
    
}

public class AIPolicy
{
    private int m_Id = -1;
    private List<AIBehavior> m_Behaviors;
    private List<AIGoalSensor> m_Sensors;
    
    public List<AIGoalSensor> Sensors => m_Sensors;
    public List<AIBehavior> Behaviors => m_Behaviors;
    
    public AIPolicy(int id)
    {
        m_Id = id;
        Init(m_Id);
    }
    public static List<int> ParseIds(string behaviorList, string splitStr)
    {
        return behaviorList.Split(splitStr)
            .Select(idStr => int.TryParse(idStr, out var idValue) ? idValue : -1)
            .Where(idValue => idValue != -1)
            .ToList();
    }

    private void Init(int id)
    {
       Tab_NpcAIPolicyRoot policyRoot = TableManager.GetNpcAIPolicyRootByID(id);
       if (policyRoot.IsNull())
       {
           Debug.LogError($"AIPolicy Init Error: Policy Root not found for ID: {id}");
           return;
       }

       Tab_NpcAIPolicy tabPolicy = TableManager.GetNpcAIPolicyByID(policyRoot.PolicyId);
       if(tabPolicy.IsNull())
       {
           Debug.LogError($"AIPolicy Init Error: Policy not found for ID: {policyRoot.PolicyId}");
           return;
       }

       List<int> behaviorIds = ParseIds(tabPolicy.BehaviorList, "|");
       InitBehaviors(behaviorIds);
       
       List<int> goalIds = ParseIds(tabPolicy.GoalSensorList, "|");
       InitGoals(goalIds);
    }
    
    private void InitBehaviors(List<int> behaviors)
    {
        m_Behaviors = new List<AIBehavior>();
        foreach (var id in behaviors)
        {
            AIBehavior behavior = new AIBehavior(id);
            m_Behaviors.Add(behavior);
        }
    }
    private void InitGoals(List<int> goals)
    {
        m_Sensors = new List<AIGoalSensor>();
        foreach (var goalId in goals)
        {
            AIGoalSensor sensor = new AIGoalSensor(goalId);
            m_Sensors.Add(sensor);
        }
    }
}

public class AIBehavior
{
    public AIBehavior(int nId)
    {
        m_Id = nId;
        Init(nId);
    }
    private void Init(int nId)
    {
        m_Conditions.Clear();
        Tab_NpcAIBehavior tabBehavior = TableManager.GetNpcAIBehaviorByID(nId);
        if (tabBehavior.IsNull())
        {
            Debug.LogError($"Init AIBehavior Error: Behavior not found for ID: {nId}");
            return;
        }
        List<int> conditionIds = AIPolicy.ParseIds(tabBehavior.ConditionList, "|");
        foreach (var conditionId in conditionIds)
        {
            AICondition condition = new AICondition(conditionId);
            m_Conditions.Add(condition);
        }
    }
    private int m_Id = -1;
    private List<AICondition> m_Conditions = new List<AICondition>();

    public int Id => m_Id;
    public List<AICondition> Conditions => m_Conditions;
}

public class AIGoalSensor
{
    public AIGoalSensor(int nId)
    {
        m_Id = nId;
        Init(m_Id);
    }
    
    private void Init(int nId)
    {
        m_Conditions.Clear();
        Tab_NpcAIGoalSensor tabSensor = TableManager.GetNpcAIGoalSensorByID(nId);
        if (tabSensor.IsNull())
        {
            Debug.LogError($"Init AIGoalSensor Error: Sensor not found for ID: {nId}");
            return;
        }
        List<int> conditionIds = AIPolicy.ParseIds(tabSensor.ConditionList, "|");
        foreach (var conditionId in conditionIds)
        {
            AICondition condition = new AICondition(conditionId);
            m_Conditions.Add(condition);
        }
    }
    
    private int m_Id = -1;
    public int Id => m_Id;
    private List<AICondition> m_Conditions = new List<AICondition>();
    public List<AICondition> Conditions => m_Conditions;
}

public class AICondition
{
    public AICondition(int nId)
    {
        m_Id = nId;
        Init(m_Id);
    }

    void Init(int nId)
    {
        m_ConditionData = TableManager.GetNpcAIConditionByID(nId);
        if (m_ConditionData.IsNull())
        {
            Debug.LogError($"Init AIConditionError, Condition not found for ID: {nId}");
        }
    }
    private int m_Id = -1;
    private Tab_NpcAICondition m_ConditionData;
    public int Id => m_Id;
    public Tab_NpcAICondition ConditionData => m_ConditionData;
}



public class BuildAIGraph
{
    enum Anchor
    {
        Left,
        Right,
        Top,
        Bottom
    }

    // 这里可以添加一些辅助方法或属性
    private static Vector2 CalPos(Vector2 centerPos, float radius, float angleStep, int index, Anchor anchor)
    {
        float angle = 0;
        int xFactor = 1;
        int yFactor = 1;
        switch (anchor)
        {
            case Anchor.Left:
                angle = 90f + (angleStep * (index));
                break;
            case Anchor.Right:
                angle = 90f - (angleStep * (index));
                xFactor = 1; 
                break; 
            case Anchor.Top:
                //这里是坐标系的问题，左上角（0，0） 右下脚为（max,max)
                angle = 180 + (angleStep * index);
                break;
            case Anchor.Bottom:
                angle = 0 + angleStep * index;
                break;
        }
        float xPos = radius * Mathf.Cos(angle * Mathf.Deg2Rad) * xFactor;
        float yPos = radius * Mathf.Sin(angle * Mathf.Deg2Rad);
        Vector2 result = new Vector2(xPos, yPos);
        result += centerPos;
        return result;
    }

    public static PolicyGraph DoBuildAIGraph(ViewManager view,  AIPolicy ai, PolicyGraph graph)
    {
        
        // 创建所有节点并建索引映射
        var nodeMap = new Dictionary<string, BaseNode>();

        Vector2 createPos = Vector2.zero; 
        // 创建Root节点
        AIRootNode rootNode = BaseNode.CreateFromType(typeof(AIRootNode), createPos) as AIRootNode;
        rootNode.SetCustomName("BuildYour AI Graph");
        view.RootNodeView = view.AddNode(rootNode) as AIRootNodeView;
        //graph.AddNode(rootNode);
        //nodeMap["root"] = rootNode;


        int sensorIndex = 0;
        float radius = 300f;
        float angleStep = ai.Sensors?.Count > 0 ? 180f / (ai.Sensors.Count+1) : 0f;
        // 创建并添加传感器节点
        foreach (var s in ai.Sensors)
        {
            // 计算传感器节点的位置
            Vector2 goalPos = CalPos(createPos, radius, angleStep, ++sensorIndex, Anchor.Left);
            AISensorNode node = BaseNode.CreateFromType(typeof(AISensorNode), goalPos) as AISensorNode;
            node.Init(s.Id);
            view.AddSensorNodeView(view.AddNode(node) as AISensorNodeView);
            graph.Connect(rootNode.GetPort("input", null), node.GetPort("output", null));
            
            int conIndex = 0;
            float cRandius = 180;
            float cAngelStep = s.Conditions?.Count > 0 ? 180f / (s.Conditions.Count + 1) : 0f;
            foreach (var con in s.Conditions)
            {
                Vector2 condPos = CalPos(goalPos, cRandius, cAngelStep, ++conIndex, Anchor.Left);
                AIConditionNodeBase c_node = BaseNode.CreateFromType(typeof(AIConditionNodeBase), condPos) as AIConditionNodeBase;
                c_node.Init(con.Id);
                view.AddConditionNodeView(view.AddNode(c_node) as AIConditionNodeBaseView);
                graph.Connect(node.GetPort("input", null),c_node.GetPort("output", null));
            }
        }
        int beIndex = 0;
        float beRadius = 300f; 
        float beAngleStep = ai.Behaviors?.Count > 0 ? 180f / (ai.Behaviors.Count + 1) : 0f;
        // 创建行为节点
        foreach (var b in ai.Behaviors)
        {
            Vector2 behaviorPos = CalPos(createPos, beRadius, beAngleStep, (++beIndex), Anchor.Right);
            AIBehaviorNodeBase node = BaseNode.CreateFromType(typeof(AIBehaviorNodeBase), behaviorPos) as AIBehaviorNodeBase;
            node.Init(b.Id);
            view.AddBehaviorNodeView(view.AddNode(node) as AIBehaviorNodeBaseView);
            graph.Connect(node.GetPort("input", null), rootNode.GetPort("output", null));
            Vector2 condPos = behaviorPos + new Vector2(200, 0);

            int conIndex = 0;
            float conRadius = 180f;
            float conAngleStep = b.Conditions?.Count > 0 ? 180f / (b.Conditions.Count + 1) : 0f;
            foreach (var con in b.Conditions)
            {
                condPos = CalPos(behaviorPos, conRadius, conAngleStep, ++conIndex, Anchor.Top);
                AIConditionNodeBase c_node = BaseNode.CreateFromType(typeof(AIConditionNodeBase), condPos) as AIConditionNodeBase;
                c_node.Init(con.Id);
                view.AddConditionNodeView(view.AddNode(c_node) as AIConditionNodeBaseView);
                graph.Connect(node.GetPort("input", null), c_node.GetPort("output", null));
            }
        }
        return graph;
    }
}


