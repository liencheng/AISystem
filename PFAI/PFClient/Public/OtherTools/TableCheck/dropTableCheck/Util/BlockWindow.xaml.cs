using System;
using System.Windows;
using System.Windows.Threading;

namespace Util
{
    /// <summary>
    /// BlockWindow.xaml 的交互逻辑
    /// </summary>
    public partial class BlockWindow : Window
    {
        private DispatcherTimer mDataTimer = null;
        private int m_DelaySecond = 0;
        public int DelaySecond
        {
            get { return m_DelaySecond; }
            set { m_DelaySecond = value; }
        }

        public BlockWindow()
        {
            InitializeComponent();
        }

        public void StartTimeDownd()
        {
            DelaySecond = 0;
            mDataTimer = new DispatcherTimer();
            mDataTimer.Tick += new EventHandler(Update);
            mDataTimer.Interval = new TimeSpan(0, 0, 1);
            mDataTimer.Start();
        }

        public void StopTimeDownd()
        {
            mDataTimer.Stop();
        }

        public void Update(object sender, EventArgs e)
        {
            m_DelaySecond++;
            if (m_DelaySecond < 60)
            {
                tbSecond.Text = Util.GetDictionary("str_common_wait_sec", m_DelaySecond);
            }
            else if (m_DelaySecond >= 60 && m_DelaySecond < 3600)
            {
                tbSecond.Text = Util.GetDictionary("str_common_wait_min", m_DelaySecond/60, m_DelaySecond%60);
            }
            else
            {
                int hour = m_DelaySecond / 3600;
                int min = (m_DelaySecond % 3600)/60;
                int sec = (m_DelaySecond % 3600) % 60;
                tbSecond.Text = Util.GetDictionary("str_common_wait_hour", hour, min, sec);
            }

//             if (m_DelaySecond > 0)
//             {
//                 m_DelaySecond--;
//                 tbSecond.Text = m_DelaySecond.ToString();
//                 tbSecond.IsEnabled = true;
//                 if (m_DelaySecond <= 0)
//                 {
//                     tbSecond.IsEnabled = false;
//                     mDataTimer.Stop();
//                     Util.CloseBlockWindow();
//                 }
//             }
//             else
//             {
//                 tbSecond.IsEnabled = false;
//                 mDataTimer.Stop();
//             }
        }

        // 点击继续的处理函数
        private void button_continue_Click(object sender, RoutedEventArgs e)
        {
            Util.CloseBlockWindow();
            if (Util.sContinueFunc != null)
            {
                Util.sContinueFunc();
            }
        }

        // 点击取消的处理函数
        private void button_cancel_Click(object sender, RoutedEventArgs e)
        {
            Util.CloseBlockWindow();
        }
    }
}
