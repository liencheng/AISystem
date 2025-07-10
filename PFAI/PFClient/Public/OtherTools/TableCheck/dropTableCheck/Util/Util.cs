using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Windows;
using System.Windows.Media.Imaging;
using System.Windows.Threading;
using TableCheck.usercontrol;

namespace Util
{
    public class Util
    {
        public delegate void ConitnueFunc();
        public static ConitnueFunc sContinueFunc = null;

        public static string GetDictionary(string strname, params object[] args)
        {
            Object szSouce = Application.Current.FindResource(strname);
            if (szSouce != null)
            {
                return string.Format(szSouce.ToString(), args);
            }
            return strname;
        }

        public static void MessageBoxNotice(string strname, params object[] args)
        {
            Object szSouce = null;
            try
            {
                szSouce = Application.Current.FindResource(strname);
            }
            catch (ResourceReferenceKeyNotFoundException)
            {
                MessageBox.Show(Application.Current.FindResource("str_common_resource_not_found").ToString());
            }
            catch (ArgumentNullException)
            {
                MessageBox.Show(Application.Current.FindResource("str_common_resource_null").ToString());
            }
            if (szSouce != null)
            {
                string str_msg = string.Format(szSouce.ToString(), args);
                MessageBox.Show(str_msg);
            }
            else
            {
                MessageBox.Show(Application.Current.FindResource("str_common_resource_null").ToString());
            }
        }

        /// <summary>
        /// 消息框提示 带按钮
        /// </summary>
        /// <param name="messageBoxText">内容字典字符串</param>
        /// <param name="caption">标题字典字符串</param>
        /// <param name="button">显示哪个按钮</param>
        public static MessageBoxResult MessageBoxNotice(string messageBoxText, string caption, MessageBoxButton button)
        {
            try
            {
                if ("" == caption)
                {
                    return MessageBox.Show(Application.Current.FindResource(messageBoxText).ToString(), "", button);
                }
                else
                {
                    return MessageBox.Show(Application.Current.FindResource(messageBoxText).ToString(), Application.Current.FindResource(caption).ToString(), button);
                }
            }
            catch (ResourceReferenceKeyNotFoundException)
            {
                return MessageBox.Show(Application.Current.FindResource("str_common_resource_not_found").ToString());
            }
            catch (ArgumentNullException)
            {
                return MessageBox.Show(Application.Current.FindResource("str_common_resource_null").ToString());
            }
        }

        /// <summary>
        /// 打开阻塞窗口
        /// </summary>
        /// <param name="msg">显示文字</param>
        /// <param name="owner">阻塞窗口父窗口 默认为MainWindow</param>
        public static void OpenBlockWindow(string msg, Window owner = null)
        {
            BlockWindow blockWindow = new BlockWindow();
            if (owner == null)
            {
                owner = Application.Current.MainWindow;
            }
            owner.IsEnabled = false;
            Random random = new Random();
            int index = random.Next(1, 6);
            string filepath = string.Format("../Res/image/wait{0}.jpg", index);
            blockWindow.button_continue.Visibility = System.Windows.Visibility.Hidden;
            blockWindow.button_cancel.Visibility = System.Windows.Visibility.Hidden;
            blockWindow.imWaiting.Source = new BitmapImage(new Uri(filepath, UriKind.Relative));
            blockWindow.imWaiting.Opacity = 0.5;
            blockWindow.tbWaiting.Text = GetDictionary(msg);
            blockWindow.Owner = owner;
            blockWindow.Show();
            blockWindow.StartTimeDownd();
        }

        /// <summary>
        /// 关闭阻塞窗口
        /// </summary>
        public static void CloseBlockWindow()
        {
            foreach (Window window in Application.Current.Windows)
            {
                if (window is BlockWindow)
                {
                    if (window.Owner != null)
                    {
                        window.Owner.IsEnabled = true;
                    }
                    BlockWindow bw = window as BlockWindow;
                    if (bw != null)
                    {
                        bw.StopTimeDownd();
                    }
                    window.Close();
                }
            }
        }

        public static void OpenAttentionWindow(string msg, string imgpath, TableCheck.Window.Warning.OnOkRet okret, Object param = null, Window owner = null)
        {
            TableCheck.Window.Warning warwindow = new TableCheck.Window.Warning();
            if (owner == null)
            {
                owner = Application.Current.MainWindow;
            }
            owner.IsEnabled = false;
            warwindow.Im_WarIcon.Source = new BitmapImage(new Uri(imgpath, UriKind.Relative));
            warwindow.Im_WarIcon.Opacity = 0.3;
            warwindow.TB_Msg.Text = msg;
            warwindow.Owner = owner;
            warwindow.mOnOkRet = okret;
            warwindow.Param = param;
            warwindow.Show();
        }

        // 数据导出到Excel文件
        public static void DataToExcelBinary(string filename, DataSet oldds)
        {
            if (oldds.Tables.Count <= 0)
            {
                MessageBoxNotice("str_common_no_data_toexport");
                return;
            }
            try
            {
                StreamWriter sw = new StreamWriter(filename, true, System.Text.Encoding.Default);
                DataTable tdr = oldds.Tables[0];
                object[] values = new object[tdr.Columns.Count];
                foreach (DataColumn dc in tdr.Columns)
                {
                    sw.Write(dc.Caption.ToString());
                    sw.Write('\t');
                }
                sw.Write("\r\n");
                foreach (DataRow dr in oldds.Tables[0].Rows)
                {
                    foreach (DataColumn dc in tdr.Columns)
                    {
                        //sw.Write("'" + dr[dc.ColumnName].ToString() + "'");
                        sw.Write(dr[dc.ColumnName].ToString());
                        sw.Write("\t");
                    }
                    sw.Write("\r\n");
                }
                sw.Flush();
                sw.Close();
                MessageBoxNotice("str_common_out_to_excel_suc");
            }
            catch(Exception ex)
            {
                string dicstr = ex.ToString();
                MessageBox.Show(dicstr);
            }
        }
    }
    
}