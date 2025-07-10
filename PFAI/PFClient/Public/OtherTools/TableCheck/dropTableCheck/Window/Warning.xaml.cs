using System.Windows;

namespace TableCheck.Window
{
    /// <summary>
    /// Warning.xaml 的交互逻辑
    /// </summary>
    public partial class Warning : System.Windows.Window
    {
        public object Param = null;
        public delegate void OnOkRet(object param);
        public OnOkRet mOnOkRet = null;

        public Warning()
        {
            InitializeComponent();
        }

        private void Bt_Continue_Click(object sender, RoutedEventArgs e)
        {
            Close();
            if (Owner != null)
            {
                Owner.IsEnabled = true;
            }

            if (mOnOkRet != null)
            {
                mOnOkRet(Param);
            }
            
        }

        private void Bt_Cancel_Click(object sender, RoutedEventArgs e)
        {
            Close();
            if (Owner != null)
            {
                Owner.IsEnabled = true;
            }
        }
    }
}
