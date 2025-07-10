using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Data;
using System.Xml.Linq;

namespace TableAnalyzer
{
    public partial class Form1 : Form
    {
        public static string TEMPLATE_PATH = "../../../AnalyzeTemplate/";

        private static AnalyzerCore analyzer = new AnalyzerCore();
        private static List<string> loadedTables = new List<string>();
        private static XElement currentProcessing = null;

        public Form1()
        {
            InitializeComponent();
            analyzer.Init();
            loadedTables = new List<string>();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //遍历模板目录，加载Combo
            DirectoryInfo dirInfo = new DirectoryInfo(TEMPLATE_PATH);
            FileInfo[] files = dirInfo.GetFiles();
            comboBox1.Items.Clear();
            foreach(FileInfo f in files)
            {
                if (f.Extension == ".xml")
                {
                    comboBox1.Items.Add(f.Name.Substring(0, f.Name.LastIndexOf('.')));
                }
            }
            comboBox1.SelectedIndex = 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filePath = Path.GetFullPath(TEMPLATE_PATH + comboBox1.SelectedItem + ".xml");
            currentProcessing = XElement.Load(filePath);
            DataTable tab = new DataTable();
            foreach (var param in currentProcessing.Element("Params").Elements("Param"))
            {
                DataColumn column = new DataColumn();
                column.ColumnName = param.Attribute("Id").Value;
                column.DataType = System.Type.GetType(param.Attribute("Type").Value);
                column.DefaultValue = param.Attribute("Default").Value;
                tab.Columns.Add(column);
            }
            tab.NewRow();
            dataGridView2.AutoGenerateColumns = true;
            dataGridView2.DataSource = tab;
        }

        private void StartCalculate()
        {
            if (currentProcessing == null)
            {
                return;
            }
            analyzer.SetParams(dataGridView2.DataSource as DataTable);
            //加载相关表格
            foreach (var tab in currentProcessing.Elements("Require"))
            {
                LoadNewTable(tab.Attribute("Name").Value);
            }
            analyzer.ExecuteSQLCommand(currentProcessing.Attribute("SQLName").Value);
            DataSet data = analyzer.GetResultTable();

            this.dataGridView1.AutoGenerateColumns = true;
            this.dataGridView1.DataSource = data.Tables[0];
        }

        private void LoadNewTable(string tabName)
        {
            if (loadedTables.Contains(tabName) == false)
            {
                analyzer.ReadTableToDB(tabName);
                loadedTables.Add(tabName);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //根据填写的参数构建参数表
            StartCalculate();
        }
    };
}
