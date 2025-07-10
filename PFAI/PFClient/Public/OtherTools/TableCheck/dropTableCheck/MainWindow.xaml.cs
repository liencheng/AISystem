using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;
using TableCheck.usercontrol;
using Module.Log;

namespace TableCheck
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : System.Windows.Window
    {
        private Dictionary<string, UserControl> UCElement = new Dictionary<string, UserControl>();
        public RecursionDrop m_RecursionDrop = new RecursionDrop();

        public MainWindow()
        {
            InitializeComponent();
            //LogModule.Init();
            InitUC();
        }

        void InitUC()
        {
            UCElement.Add("str_tab_header7", m_RecursionDrop);

            foreach (var pair in UCElement)
            {
                TabItem tmpItem = new TabItem();
                tmpItem.Header = Util.Util.GetDictionary(pair.Key);
                tmpItem.Content = pair.Value;
                tmpItem.Margin = new Thickness(0, 1, 1, 1);
                FunctionListTab.Items.Add(tmpItem);
            }
        }

        private void TabItemSelect(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}
