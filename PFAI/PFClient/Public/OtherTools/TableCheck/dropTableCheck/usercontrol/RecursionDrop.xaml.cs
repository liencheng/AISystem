using GlobalDef;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace TableCheck.usercontrol
{
    /// <summary>
    /// RecursionDrop.xaml 的交互逻辑
    /// </summary>
    public partial class RecursionDrop : UserControl
    {
        public enum EDropType
        {
            ERate = 0,      // 概率掉落
            EWeight = 1,    // 权重掉落
        }
        public Dictionary<int, string> mItemList = new Dictionary<int, string>();

        public class DropItem : INotifyPropertyChanged
        {
            public int index = -1;
            public int mDropType = -1;
            private string mStrDropType = "";
            public string DropType 
            {
                get { return mStrDropType; }
                set
                {
                    mStrDropType = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("DropType"));
                    }
                }
            }
            private int mItemId = -1;
            public int ItemId   
            {
                get { return mItemId; } 
                set
                {
                    mItemId = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("ItemId"));
                    }
                }
            }
            private string mItemName = "";
            public string ItemName 
            {
                get { return mItemName; } 
                set
                {
                    mItemName = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("ItemName"));
                    }
                }
            }
            private double mDropVal = 0f;
            public double DropVal 
            {
                get { return mDropVal; }
                set
                {
                    mDropVal = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("DropVal"));
                    }
                }
            }
            private int mCount = 0;
            public int Count 
            {
                get { return mCount; }
                set
                {
                    mCount = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("Count"));
                    }
                }
            }
            public bool IsPrecious = false;
            private string mStrPrecious = "";
            public string StrPrecious 
            {
                get { return mStrPrecious; } 
                set
                {
                    mStrPrecious = value;
                    if (PropertyChanged != null)
                    {
                        PropertyChanged(this, new PropertyChangedEventArgs("StrPrecious"));
                    }
                }
            }

            protected internal virtual void OnPropertyChanged(string propertyName)
            {
                if (PropertyChanged != null)
                {
                    PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
                }
            }
            public event PropertyChangedEventHandler PropertyChanged;
        }

        private ObservableCollection<DropItem> mDropList = new ObservableCollection<DropItem>();

        enum EColIndex
        {
            Id = 0,
            Desc,
            Type,
            DropMax,
            RandTimes,
            ItemMax,
            NotifyId,
            BindRate,
            WeightTimes,
            DropType_1,
            ItemID_1,
            ItemDropRate_1,
            Count_1,
            IsPrecious_1,
            DropType_2,
            ItemID_2,
            ItemDropRate_2,
            Count_2,
            IsPrecious_2,
            DropType_3,
            ItemID_3,
            ItemDropRate_3,
            Count_3,
            IsPrecious_3,
            DropType_4,
            ItemID_4,
            ItemDropRate_4,
            Count_4,
            IsPrecious_4,
            DropType_5,
            ItemID_5,
            ItemDropRate_5,
            Count_5,
            IsPrecious_5,
            DropType_6,
            ItemID_6,
            ItemDropRate_6,
            Count_6,
            IsPrecious_6,
            DropType_7,
            ItemID_7,
            ItemDropRate_7,
            Count_7,
            IsPrecious_7,
            DropType_8,
            ItemID_8,
            ItemDropRate_8,
            Count_8,
            IsPrecious_8,
            DropType_9,
            ItemID_9,
            ItemDropRate_9,
            Count_9,
            IsPrecious_9,
            DropType_10,
            ItemID_10,
            ItemDropRate_10,
            Count_10,
            IsPrecious_10,
            DropType_11,
            ItemID_11,
            ItemDropRate_11,
            Count_11,
            IsPrecious_11,
            DropType_12,
            ItemID_12,
            ItemDropRate_12,
            Count_12,
            IsPrecious_12,
            DropType_13,
            ItemID_13,
            ItemDropRate_13,
            Count_13,
            IsPrecious_13,
            DropType_14,
            ItemID_14,
            ItemDropRate_14,
            Count_14,
            IsPrecious_14,
            DropType_15,
            ItemID_15,
            ItemDropRate_15,
            Count_15,
            IsPrecious_15,
            DropType_16,
            ItemID_16,
            ItemDropRate_16,
            Count_16,
            IsPrecious_16,
            DropType_17,
            ItemID_17,
            ItemDropRate_17,
            Count_17,
            IsPrecious_17,
            DropType_18,
            ItemID_18,
            ItemDropRate_18,
            Count_18,
            IsPrecious_18,
            DropType_19,
            ItemID_19,
            ItemDropRate_19,
            Count_19,
            IsPrecious_19,
            DropType_20,
            ItemID_20,
            ItemDropRate_20,
            Count_20,
            IsPrecious_20,
            DropLuckyValueId,
            EColMax
        }

        public class RowData
        {
            public string Desc = "";
            public int Type = -1;
            public int DropMax = -1;
            public int RandTimes = 1;
            public int ItemMax = 1;
            public int NotifyId = -1;
            public double BindRate = 1f;
            public int WeightTimes = -1;
            public int DropLuckyValueId = -1;
            public List<int> DropTypeList = new List<int>();
            public List<int> ItemIDList = new List<int>();
            public List<double> DropRateList = new List<double>();
            public List<int> CountList = new List<int>();
            public List<int> IsPreciousList = new List<int>();
        }
        public List<int> mBaseIdList = new List<int>();
        public List<string> mBaseHeads = new List<string>();
        public Dictionary<int, RowData> mBaseTableData = new Dictionary<int, RowData>();

        public List<int> mResetIdList = new List<int>();
        public List<string> mResetHeads = new List<string>();
        public Dictionary<int, RowData> mResetTableData = new Dictionary<int, RowData>();
        private RowData mImportRd = null;
        private bool? mIsReset = null;
        private string mFillStr = "0.##########";

        class ChildDrop :INotifyPropertyChanged
        {
            public int ChildId { get; set; }
            public string StrVersion { get; set; }
            public int MumId { get; set; }
            public string MumDesc { get; set; }
            protected internal virtual void OnPropertyChanged(string propertyName)
            {
                if (PropertyChanged != null)
                {
                    PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
                }
            }
            public event PropertyChangedEventHandler PropertyChanged;
        }
        private ObservableCollection<ChildDrop> mWaitingList = new ObservableCollection<ChildDrop>();

        public RecursionDrop()
        {
            InitializeComponent();

            LV_DropList.ItemsSource = mDropList;
            LV_ChildWaitList.ItemsSource = mWaitingList;
            InitItemList();
            InitTableData(false, mBaseTableData, mBaseIdList);
            mWaitingList.Clear();
        }

        void InitItemList()
        {
            mItemList.Clear();
            string itempath = "../../PublicTables/CommonItem.txt";
            try
            {
                StreamReader sr = new StreamReader(itempath, System.Text.Encoding.Default);

                int rows = 0;
                int itemid = -1;

                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    rows++;
                    if (rows <= 4)
                    {
                        continue;
                    }
                    if (line != null)
                    {
                        string[] cols = line.Split('\t');
                        if(cols[0].Contains("#"))
                        {
                            continue;
                        }
                        if (int.TryParse(cols[0], out itemid) == false)
                        {
                            Util.Util.MessageBoxNotice("str_recursiondrop_32", rows);
                            break;
                        }
                        mItemList.Add(itemid, cols[2]);
                    }
                }
                sr.Close();
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        private void BT_AddDrop_Click(object sender, RoutedEventArgs e)
        {
            if (CB_DropType.SelectedIndex == -1)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_33");
                return;
            }
            //if (mIsReset == null)
            //{
            //    Util.Util.MessageBoxNotice("str_recursiondrop_73");
            //    return;
            //}

            Window.DropItemWindow dWindow = new Window.DropItemWindow();
            MainWindow curWindow = Application.Current.MainWindow as MainWindow;
            dWindow.Owner = curWindow;
            dWindow.mItemList = mItemList;
            dWindow.IsRate = CB_DropType.SelectedIndex == (int)ERandomType.ER_Rate;
            dWindow.mOnOKClick = AddDropItemRet;
            dWindow.Show();
        }

        public void AddDropItemRet(List<DropItem> dropList)
        {
            foreach(var di in dropList)
            { 
                di.index = mDropList.Count;
                if (di.mDropType == (int)EDropItemType.EDI_Drop)
                {
                    di.ItemName = GetDescById(mIsReset == true, di.ItemId);
                }
                mDropList.Add(di);
            }
            TB_DropCount.Text = mDropList.Count.ToString();
        }

        private void Bt_ClearDropList_Click(object sender, RoutedEventArgs e)
        {
            mDropList.Clear();
            TB_DropCount.Text = "";
        }

        private void Bt_Delete_Click(object sender, RoutedEventArgs e)
        {
            var btn = sender as Button;
            DropItem di = btn.DataContext as DropItem;
            int index = di.index;
            mDropList.Remove(di);
            for(int i = index; i < mDropList.Count; ++i)
            {
                mDropList[i].index = i;
            }
            TB_DropCount.Text = mDropList.Count.ToString();
        }

        private void Bt_Modify_Click(object sender, RoutedEventArgs e)
        {
            var btn = sender as Button;
            DropItem di = btn.DataContext as DropItem;

            Window.DropModify dm = new Window.DropModify();
            MainWindow curWindow = Application.Current.MainWindow as MainWindow;
            dm.Owner = curWindow;

            dm.mItemList = mItemList;
            string strrate = "";
            if (CB_DropType.SelectedIndex == (int)ERandomType.ER_Rate)
            {
                strrate = Util.Util.GetDictionary("str_recursiondrop_16");
            }
            else if (CB_DropType.SelectedIndex == (int)ERandomType.ER_Weight)
            {
                strrate = Util.Util.GetDictionary("str_recursiondrop_17");
            }
            dm.dropItem = di;
            dm.StrRate = strrate;
            dm.mOnModify = ModifyRet;
            dm.Show();
            dm.InitData();
        }

        void ModifyRet(DropItem di)
        {
            if (di == null)
            {
                return;
            }
            int index = di.index;
            if (index >= 0 && index < mDropList.Count)
            {
                mDropList[index] = di;
                if (di.mDropType == (int)EDropItemType.EDI_Drop)
                {
                    mDropList[index].ItemName = GetDescById(mIsReset == true, di.ItemId);
                }
            }
        }

        private void BT_ImportDropById_Click(object sender, RoutedEventArgs e)
        {
            string str_id = TB_TemplateId.Text.Trim();
            if (string.IsNullOrEmpty(str_id))
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_71");
                return;
            }
            int tmp_id = -1;
            if (int.TryParse(str_id, out tmp_id) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_72");
                return;
            }
            
            if (mIsReset == true)
            {
                if (mResetTableData.ContainsKey(tmp_id) == false)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_74");
                    return;
                }
                mImportRd = mResetTableData[tmp_id];
            }
            else
            {
                if (mBaseTableData.ContainsKey(tmp_id) == false)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_78");
                    return;
                }
                mImportRd = mBaseTableData[tmp_id];
            }
            
            TB_DropId.Text = tmp_id.ToString();
            TB_Desc.Text = mImportRd.Desc;
            CB_DropType.SelectedIndex = mImportRd.Type;
            TB_DropMax.Text = mImportRd.DropMax.ToString();
            TB_NotifyId.Text = mImportRd.NotifyId.ToString();
            TB_RandTimes.Text = mImportRd.RandTimes.ToString();
            TB_BindRate.Text = mImportRd.BindRate.ToString();
            TB_WeightTimes.Text = mImportRd.WeightTimes.ToString();
            TB_LuckValue.Text = mImportRd.DropLuckyValueId.ToString();

            mDropList.Clear();
            for (int i = 0; i < mImportRd.DropTypeList.Count && i < mImportRd.ItemIDList.Count && i < mImportRd.DropRateList.Count && i < mImportRd.CountList.Count && i < mImportRd.IsPreciousList.Count; ++i)
            {
                if (mImportRd.DropTypeList[i] == -1)
                {
                    continue;
                }
                DropItem di = new DropItem();
                di.mDropType = mImportRd.DropTypeList[i];
                di.ItemId = mImportRd.ItemIDList[i];
                if (di.mDropType == (int)EDropItemType.EDI_Item)
                {
                    di.DropType = Util.Util.GetDictionary("str_recursiondrop_11");
                    if (mItemList.ContainsKey(di.ItemId))
                    {
                        di.ItemName = mItemList[di.ItemId];
                    }
                    else
                    {
                        di.ItemName = Util.Util.GetDictionary("str_recursiondrop_76");
                    }
                }
                else if (di.mDropType == (int)EDropItemType.EDI_Drop)
                {
                    di.DropType = Util.Util.GetDictionary("str_recursiondrop_12");
                    di.ItemName = GetDescById(mIsReset==true, di.ItemId);
                }
                else
                {
                    di.DropType = Util.Util.GetDictionary("str_recursiondrop_75");

                }
                di.DropVal = mImportRd.DropRateList[i];
                di.Count = mImportRd.CountList[i];
                di.IsPrecious = mImportRd.IsPreciousList[i] == 1;
                di.StrPrecious = di.IsPrecious ? Util.Util.GetDictionary("str_recursiondrop_21") : Util.Util.GetDictionary("str_recursiondrop_22");
                di.index = i;
                mDropList.Add(di);
            }
            TB_DropCount.Text = mDropList.Count.ToString();
        }

        string GetDescById(bool isReset, int id)
        {
            if (isReset)
            {
                if (mResetTableData.ContainsKey(id))
                {
                    return mResetTableData[id].Desc;
                }
            }
            else
            {
                if (mBaseTableData.ContainsKey(id))
                {
                    return mBaseTableData[id].Desc;
                }
            }
            return Util.Util.GetDictionary("str_recursiondrop_80");
        }

        private void InitTableData(bool isRest, Dictionary<int, RowData> tabdata, List<int> idlist)
        {
            string tabPath = "";
            if (isRest)
            {
                tabPath = "../../../../Reset/ServerResetTables/RecursionDrop.txt";
            }
            else
            {
                tabPath = "../../ServerTables/RecursionDrop.txt";
            }

            tabdata.Clear();
            int lineno = 0;
            string strline = "";
            string errstr = "";
            int tmp_id = -1;
            int tmp_droptype = -1;
            int tmp_dropid = -1;
            double tmp_droprate = 0f;
            int tmp_count = -1;
            int tmp_isprecious = -1;

            try
            {
                StreamReader sr = new StreamReader(tabPath, System.Text.Encoding.Default);
                while ((strline = sr.ReadLine()) != null)
                {
                    lineno++;
                    if (lineno <= 4)
                    {
                        if (isRest)
                        {
                            mResetHeads.Add(strline);
                        }
                        else
                        {
                            mBaseHeads.Add(strline);
                        }
                        continue;
                    }
                    string[] cols = strline.Split('\t');
                    if (cols.Length < (int)EColIndex.EColMax)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_57", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    string str = cols[(int)EColIndex.Id].Trim();
                    if (str.Contains("#"))
                    {
                        continue;
                    }
                    if (int.TryParse(cols[(int)EColIndex.Id].Trim(), out tmp_id) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_58", isRest ? "Reset" : "Base", lineno);
                        break;
                    }

                    RowData rd = new RowData();
                    rd.Desc = cols[(int)EColIndex.Desc].Trim();
                    if (int.TryParse(cols[(int)EColIndex.Type].Trim(), out rd.Type) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_59", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (int.TryParse(cols[(int)EColIndex.DropMax].Trim(), out rd.DropMax) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_60", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (int.TryParse(cols[(int)EColIndex.RandTimes].Trim(), out rd.RandTimes) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_61", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (int.TryParse(cols[(int)EColIndex.ItemMax].Trim(), out rd.ItemMax) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_62", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (int.TryParse(cols[(int)EColIndex.NotifyId].Trim(), out rd.NotifyId) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_63", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (double.TryParse(cols[(int)EColIndex.BindRate].Trim(), out rd.BindRate) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_64", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (int.TryParse(cols[(int)EColIndex.WeightTimes].Trim(), out rd.WeightTimes) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_123", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    int group = 1;
                    for (int index = (int)EColIndex.DropType_1; index < (int)EColIndex.DropLuckyValueId;)
                    {
                        if (int.TryParse(cols[index].Trim(), out tmp_droptype) == false)
                        {
                            errstr = Util.Util.GetDictionary("str_recursiondrop_65", isRest ? "Reset" : "Base", lineno, group);
                            break;
                        }
                        index++;
                        if (int.TryParse(cols[index].Trim(), out tmp_dropid) == false)
                        {
                            errstr = Util.Util.GetDictionary("str_recursiondrop_66", isRest ? "Reset" : "Base", lineno, group);
                            break;
                        }
                        index++;
                        if (double.TryParse(cols[index].Trim(), out tmp_droprate) == false)
                        {
                            errstr = Util.Util.GetDictionary("str_recursiondrop_67", isRest ? "Reset" : "Base", lineno, group);
                            break;
                        }
                        index++;
                        if (int.TryParse(cols[index].Trim(), out tmp_count) == false)
                        {
                            errstr = Util.Util.GetDictionary("str_recursiondrop_68", isRest ? "Reset" : "Base", lineno, group);
                            break;
                        }
                        index++;
                        if (int.TryParse(cols[index].Trim(), out tmp_isprecious) == false)
                        {
                            errstr = Util.Util.GetDictionary("str_recursiondrop_69", isRest ? "Reset" : "Base", lineno, group);
                            break;
                        }
                        rd.DropTypeList.Add(tmp_droptype);
                        rd.ItemIDList.Add(tmp_dropid);
                        rd.DropRateList.Add(tmp_droprate);
                        rd.CountList.Add(tmp_count);
                        rd.IsPreciousList.Add(tmp_isprecious);

                        index++;
                        group++;
                    }
                    if (int.TryParse(cols[(int)EColIndex.DropLuckyValueId].Trim(), out rd.DropLuckyValueId) == false)
                    {
                        errstr = Util.Util.GetDictionary("str_recursiondrop_124", isRest ? "Reset" : "Base", lineno);
                        break;
                    }
                    if (string.IsNullOrEmpty(errstr) == false)
                    {
                        break;
                    }
                    tabdata.Add(tmp_id, rd);
                    idlist.Add(tmp_id);
                }

                sr.Close();

                // Util.Util.CloseBlockWindow();
                if (string.IsNullOrEmpty(errstr) == false)
                {
                    MessageBox.Show(errstr);
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        //private void RB_Base_Checked(object sender, RoutedEventArgs e)
        //{
        //    if (RB_Base.IsChecked == true)
        //    {
        //        mIsReset = false;
        //    }
        //}

        RowData GenerateRow(out int dropid, bool isreset = false)
        {
            dropid = -1;
            string str_dropid = TB_DropId.Text.Trim();
            if (string.IsNullOrEmpty(str_dropid))
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_1");
                return null;
            }
            int tmp_id = -1;
            if (int.TryParse(str_dropid, out tmp_id) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_83");
                return null;
            }
            if (tmp_id <= 0)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_83");
                return null;
            }
            if (TB_Desc.Text.Trim() == "")
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_85");
                return null;
            }
            if (CB_DropType.SelectedIndex == -1)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_33");
                return null;
            }
            if (CB_DropType.SelectedIndex != (int)ERandomType.ER_Rate && CB_DropType.SelectedIndex != (int)ERandomType.ER_Weight)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_86");
                return null;
            }
            if (TB_DropMax.Text.Trim() == "")
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_87");
                return null;
            }
            int dropmax = -1;
            if (int.TryParse(TB_DropMax.Text.Trim(), out dropmax) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_87");
                return null;
            }
            if (TB_RandTimes.Text.Trim() == "")
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_88");
                return null;
            }
            int randtimes = -1;
            if (int.TryParse(TB_RandTimes.Text.Trim(), out randtimes) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_88");
                return null;
            }
            if (randtimes <= 0)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_88");
                return null;
            }
            if (TB_NotifyId.Text.Trim() == "")
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_89");
                return null;
            }
            int notifyid = -1;
            if (int.TryParse(TB_NotifyId.Text.Trim(), out notifyid) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_89");
                return null;
            }
            if (TB_BindRate.Text.Trim() == "")
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_90");
                return null;
            }
            double bindrate = 0f;
            if (double.TryParse(TB_BindRate.Text.Trim(), out bindrate) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_91");
                return null;
            }
            if (bindrate < 0f || bindrate > 1f)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_91");
                return null;
            }
            int weightTimes = 0;
            if(int.TryParse(TB_WeightTimes.Text.Trim(), out weightTimes) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_WeightTimes");
                return null;
            }
            int luckValue = 0;
            if (int.TryParse(TB_LuckValue.Text.Trim(), out luckValue) == false)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_LuckValue");
                return null;
            }

            if (mDropList.Count <= 0)
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_92");
                return null;
            }

            RowData rd = new RowData();
            rd.Desc = TB_Desc.Text;
            rd.Type = CB_DropType.SelectedIndex;
            rd.DropMax = dropmax;
            rd.RandTimes = randtimes;
            rd.NotifyId = notifyid;
            rd.BindRate = bindrate;
            rd.WeightTimes = weightTimes;
            rd.DropLuckyValueId = luckValue;
            rd.ItemMax = 0;
            foreach(var da in mDropList)
            {
                if (da.mDropType != (int)EDropItemType.EDI_Item && da.mDropType != (int)EDropItemType.EDI_Drop)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_93", rd.ItemMax + 1);
                    return null;
                }
                if (da.ItemId < 0)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_102", rd.ItemMax + 1);
                    return null;
                }
                if (rd.Type == (int)ERandomType.ER_Rate)
                {
                    if (da.DropVal <= 0f || da.DropVal > 10f)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_103", rd.ItemMax + 1);
                        return null;
                    }
                }
                else
                {
                    if (da.DropVal < 1f)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_104", rd.ItemMax + 1);
                        return null;
                    }
                }
                if (da.Count <= 0)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_105", rd.ItemMax + 1);
                    return null;
                }
                if (da.mDropType == (int)EDropItemType.EDI_Item)
                {
                    if (mItemList.ContainsKey(da.ItemId) == false)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_93", rd.ItemMax + 1);
                        return null;
                    }
                }
                else
                {
                        if (mBaseTableData.ContainsKey(da.ItemId) == false)
                        {
                            ChildDrop cd = new ChildDrop();
                            cd.ChildId = da.ItemId;
                            cd.StrVersion = Util.Util.GetDictionary("str_recursiondrop_100");
                            cd.MumId = tmp_id;
                            cd.MumDesc = rd.Desc;
                            if (IsInChildWaitingList(cd)== false)
                            {
                                mWaitingList.Add(cd);
                            }
                        }
                }
                rd.DropTypeList.Add(da.mDropType);
                rd.ItemIDList.Add(da.ItemId);
                rd.DropRateList.Add(da.DropVal);
                rd.CountList.Add(da.Count);
                rd.IsPreciousList.Add(da.IsPrecious ? 1 : 0);
                rd.ItemMax++;
            }

            dropid = tmp_id;
            return rd;
        }

        bool IsInChildWaitingList(ChildDrop cd)
        {
            foreach(var val in mWaitingList)
            {
                if (cd.ChildId == val.ChildId)
                {
                    return true;
                }
            }
            return false;
        }

        string GetStrLineByRd(RowData rd, int id)
        {
            if (rd == null)
            {
                return "";
            }
            string str_pre = string.Format("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}", id, rd.Desc, rd.Type, rd.DropMax, rd.RandTimes, rd.ItemMax, rd.NotifyId, rd.BindRate.ToString(mFillStr),rd.WeightTimes);
            string str_drop = "";
            for(int i = 0; i < rd.DropTypeList.Count && i < rd.ItemIDList.Count && i < rd.DropRateList.Count && i < rd.CountList.Count && i < rd.IsPreciousList.Count; ++i)
            {
                str_drop += string.Format("\t{0}\t{1}\t{2}\t{3}\t{4}", rd.DropTypeList[i], rd.ItemIDList[i], rd.DropRateList[i].ToString(mFillStr), rd.CountList[i], rd.IsPreciousList[i]);
            }
            string str_post = "";
            for (int i = rd.DropTypeList.Count; i < 20; ++i)
            {
                str_post += string.Format("\t-1\t-1\t-1\t-1\t0");
            }
            string str_last = string.Format("\t{0}", rd.DropLuckyValueId);
            str_post += str_last;
            string strline = string.Format("{0}{1}{2}", str_pre, str_drop, str_post);
            return strline;
        }

        bool WriteToFile(string fpath, int lineno, RowData rd, int id, List<string> heads, Dictionary<int, RowData> rows, List<int>lineids)
        {
            StreamWriter sw = null;
            if (rd == null)
            {
                // 重新写入
                sw = new StreamWriter(fpath, false, System.Text.Encoding.Default);
                foreach (var strrow in heads)
                {
                    sw.WriteLine(strrow);
                }
                for (int i = 0; i < lineids.Count; ++i)
                {
                    string strline = "";
                    int tmpid = lineids[i];
                    if (rows.ContainsKey(tmpid))
                    {
                        strline = GetStrLineByRd(rows[tmpid], tmpid);
                    }
                    sw.WriteLine(strline);
                }
            }
            else if (lineno == -1)
            {
                // 追加到行尾
                sw = new StreamWriter(fpath, true, System.Text.Encoding.Default);
                string strline = GetStrLineByRd(rd, id);
                sw.WriteLine(strline);

                rows.Add(id, rd);
                lineids.Add(id);
            }
            else
            {
                // 指定行插入
                sw = new StreamWriter(fpath, false, System.Text.Encoding.Default);
                foreach(var strrow in heads)
                {
                    sw.WriteLine(strrow);
                }

                for (int i = 0; i < lineids.Count; ++i)
                {
                    string strline = "";
                    int tmpid = lineids[i];
                    if (rows.ContainsKey(tmpid))
                    {
                        strline = GetStrLineByRd(rows[tmpid], tmpid);
                    }
                    sw.WriteLine(strline);

                    if (lineno == tmpid)
                    {
                        strline = GetStrLineByRd(rd, id);
                        sw.WriteLine(strline);
                    }
                }

                rows.Add(id, rd);
                lineids.Insert(lineno, id);
            }

            sw.Flush();
            sw.Close();
            return true;
        }

        public class ParamObj
        {
            public int Id = -1;
            public int LineNo = -1;
            public RowData Rd = null;
            public bool IsReset = false;
            public ParamObj(int id, int lineno, RowData rd, bool isreset)
            {
                Id = id;
                LineNo = lineno;
                Rd = rd;
                IsReset = isreset;
            }
        }

        private void BT_WriteToBase_Click(object sender, RoutedEventArgs e)
        {
            int id = -1;
            RowData rd = GenerateRow(out id, false);
            if (rd == null)
            {
                return;
            }
            int lineno = -1;
            if (mBaseTableData.ContainsKey(id))
            {
                // 修改原有的行
                Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_112", id), "../Res/image_drop/war_modify.png", ModifyExist, new ParamObj(id, lineno, rd, false));
            }
            else
            {
                string str_line = TB_LineNo.Text.Trim();
                if (string.IsNullOrEmpty(str_line))
                {
                    // 插入表格最后
                    Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_107"), "../Res/image_drop/jingdian_add.png", AddToFile, new ParamObj(id, lineno, rd, false));
                }
                else
                {
                    // 插入指定Id之后
                    if (int.TryParse(str_line, out lineno) == false)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_108");
                        return;
                    }
                    Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_106", lineno), "../Res/image_drop/jingdian_insert.png", AddToFile, new ParamObj(id, lineno, rd, false));
                }
            }

            
        }

        private void AddToFile(object param)
        {
            ParamObj po = param as ParamObj;
            if (po != null)
            {
                Util.Util.OpenBlockWindow("str_recursiondrop_109");
                if (po.IsReset)
                {
                    WriteToFile("../../Reset/ServerResetTables/RecursionDrop.txt", po.LineNo, po.Rd, po.Id, mResetHeads, mResetTableData, mResetIdList);
                }
                else
                {
                    WriteToFile("../../ServerTables/RecursionDrop.txt", po.LineNo, po.Rd, po.Id, mBaseHeads, mBaseTableData, mBaseIdList);
                }    
                Util.Util.CloseBlockWindow();
            }
        }

        private void ModifyExist(object param)
        {
            ParamObj po = param as ParamObj;
            if (po != null)
            {
                int id = po.Id;
                if (po.IsReset)
                {
                    if (mResetTableData.ContainsKey(id))
                    {
                        mResetTableData[id] = po.Rd;
                    }
                    Util.Util.OpenBlockWindow("str_recursiondrop_109");
                    WriteToFile("../../Reset/ServerResetTables/RecursionDrop.txt", -1, null, id, mResetHeads, mResetTableData, mResetIdList);
                    Util.Util.CloseBlockWindow();
                }
                else
                {
                    if (mBaseTableData.ContainsKey(id))
                    {
                        mBaseTableData[id] = po.Rd;
                    }
                    Util.Util.OpenBlockWindow("str_recursiondrop_109");
                    WriteToFile("../../ServerTables/RecursionDrop.txt", -1, null, id, mBaseHeads, mBaseTableData, mBaseIdList);
                    Util.Util.CloseBlockWindow();
                }
            }
        }

        private void BT_WriteToReset_Click(object sender, RoutedEventArgs e)
        {
            int id = -1;
            RowData rd = GenerateRow(out id, true);
            if (rd == null)
            {
                return;
            }
            int lineno = -1;
            if (mResetTableData.ContainsKey(id))
            {
                // 修改原有的行
                Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_113", id), "./Res/image_drop/war_modify.png", ModifyExist, new ParamObj(id, lineno, rd, true));
            }
            else
            {
                // 新行写入
                string str_line = TB_LineNo.Text.Trim();
                if (string.IsNullOrEmpty(str_line))
                {
                    Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_111"), "./Res/image_drop/chongzhi_add.png", AddToFile, new ParamObj(id, lineno, rd, true));
                }
                else
                {
                    if (int.TryParse(str_line, out lineno) == false)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_108");
                        return;
                    }
                    Util.Util.OpenAttentionWindow(Util.Util.GetDictionary("str_recursiondrop_110", lineno), "./Res/image_drop/chongzhi_insert.png", AddToFile, new ParamObj(id, lineno, rd, true));
                }
            }
        }

        private void Bt_ChildConfig_Click(object sender, RoutedEventArgs e)
        {
            var btn = sender as Button;
            ChildDrop cd = btn.DataContext as ChildDrop;

            TB_DropId.Text = cd.ChildId.ToString();
            TB_Desc.Text = "";
            CB_DropType.SelectedIndex = -1;
            TB_DropMax.Text = "";
            TB_NotifyId.Text = "-1";
            TB_RandTimes.Text = "1";
            TB_BindRate.Text = "";
            mDropList.Clear();
            TB_DropCount.Text = "";

            mWaitingList.Remove(cd);
        }

        private void RB_AddNew_Checked(object sender, RoutedEventArgs e)
        {
            if (RB_AddNew.IsChecked == true)
            {
                TB_TemplateId.Visibility = Visibility.Hidden;
                BT_ImportDropById.Visibility = Visibility.Hidden;
                TB_JianTou.Visibility = Visibility.Hidden;
                TB_InputDropId.Visibility = Visibility.Visible;
                TB_InputDropId2.Visibility = Visibility.Hidden;
                TB_AddNewDes.Visibility = Visibility.Visible;
                TB_LineNo.Visibility = Visibility.Visible;
                TB_DropId.IsEnabled = true;
            }
        }

        private void RB_ModifyExist_Checked(object sender, RoutedEventArgs e)
        {
            if (RB_ModifyExist.IsChecked == true)
            {
                TB_TemplateId.Visibility = Visibility.Visible;
                BT_ImportDropById.Visibility = Visibility.Visible;
                TB_JianTou.Visibility = Visibility.Visible;
                TB_InputDropId.Visibility = Visibility.Hidden;
                TB_InputDropId2.Visibility = Visibility.Visible;
                TB_AddNewDes.Visibility = Visibility.Hidden;
                TB_LineNo.Visibility = Visibility.Hidden;
                TB_DropId.IsEnabled = true;
            }
        }
    }
}
