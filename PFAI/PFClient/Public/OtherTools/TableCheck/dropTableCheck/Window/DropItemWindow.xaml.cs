using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Windows;
using System.Windows.Controls;
using GlobalDef;

namespace TableCheck.Window
{
    /// <summary>
    /// DropItem.xaml 的交互逻辑
    /// </summary>
    public partial class DropItemWindow : System.Windows.Window
    {
        
        private ObservableCollection<DropTypeData> mDropTypeList = new ObservableCollection<DropTypeData>();


        public bool mIsReset = false;
        public Dictionary<int, string> mItemList = new Dictionary<int, string>();
        private bool mIsRate = true;
        public bool IsRate
        {
            get { return mIsRate; }
            set
            {
                mIsRate = value;
                if (mIsRate)
                {
                    TB_InputRate1.Text = Util.Util.GetDictionary("str_recursiondrop_16");
                    TB_InputRate2.Text = Util.Util.GetDictionary("str_recursiondrop_16");
                    TB_InputRate3.Text = Util.Util.GetDictionary("str_recursiondrop_16");
                    TB_InputRate4.Text = Util.Util.GetDictionary("str_recursiondrop_16");
                }
                else
                {
                    TB_InputRate1.Text = Util.Util.GetDictionary("str_recursiondrop_17");
                    TB_InputRate2.Text = Util.Util.GetDictionary("str_recursiondrop_17");
                    TB_InputRate3.Text = Util.Util.GetDictionary("str_recursiondrop_17");
                    TB_InputRate4.Text = Util.Util.GetDictionary("str_recursiondrop_17");
                }
            }
        }

        public delegate void OKRet(List<usercontrol.RecursionDrop.DropItem> dropList);
        public OKRet mOnOKClick = null;

        public DropItemWindow()
        {
            InitializeComponent();

            DropTypeData da1 = new DropTypeData();
            da1.DropType = (int)EDropItemType.EDI_Item;
            da1.DropTypeName = Util.Util.GetDictionary("str_recursiondrop_11");
            mDropTypeList.Add(da1);

            DropTypeData da2 = new DropTypeData();
            da2.DropType = (int)EDropItemType.EDI_Drop;
            da2.DropTypeName = Util.Util.GetDictionary("str_recursiondrop_12");
            mDropTypeList.Add(da2);

            CB_DropType1.ItemsSource = mDropTypeList;
            CB_DropType2.ItemsSource = mDropTypeList;
            CB_DropType3.ItemsSource = mDropTypeList;
            CB_DropType4.ItemsSource = mDropTypeList;

            Lv_ItemList.ItemsSource = mItemSearchList;
        }

        void ShowItemName(TextBlock tb_name, TextBox tb_id)
        {
            if (tb_id.Text == "")
            {
                tb_name.Text = "";
            }
            int itemid = -1;
            if (int.TryParse(tb_id.Text, out itemid))
            {
                if (mItemList.ContainsKey(itemid))
                {
                    tb_name.Text = mItemList[itemid];
                }
                else
                {
                    tb_name.Text = Util.Util.GetDictionary("str_recursiondrop_76");
                }
            }
        }

        private void TB_ItemId1_TextChanged(object sender, TextChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType1.SelectedItem as DropTypeData;
            if (dtd != null && dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                ShowItemName(TB_ItemName1, TB_ItemId1);
            }
            else
            {
                TB_ItemName1.Text = "";
            }
        }

        private void TB_ItemId2_TextChanged(object sender, TextChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType2.SelectedItem as DropTypeData;
            if (dtd != null && dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                ShowItemName(TB_ItemName2, TB_ItemId2);
            }
            else
            {
                TB_ItemName2.Text = "";
            }
        }

        private void TB_ItemId3_TextChanged(object sender, TextChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType3.SelectedItem as DropTypeData;
            if (dtd != null && dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                ShowItemName(TB_ItemName3, TB_ItemId3);
            }
            else
            {
                TB_ItemName3.Text = "";
            }
        }

        private void TB_ItemId4_TextChanged(object sender, TextChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType4.SelectedItem as DropTypeData;
            if (dtd != null && dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                ShowItemName(TB_ItemName4, TB_ItemId4);
            }
            else
            {
                TB_ItemName4.Text = "";
            }
        }

        bool GenerateDropList(List<usercontrol.RecursionDrop.DropItem> dropList, DropTypeData td, TextBox id, TextBox rate, TextBox count, ComboBox isprecious, int index)
        {
            int dropitemid = -1;
            if (int.TryParse(id.Text.Trim(), out dropitemid))
            {
                double droprate = 0f;
                if (mIsRate)
                {
                    if (double.TryParse(rate.Text.Trim(), out droprate))
                    {
                        if (droprate > 10f)
                        {
                            Util.Util.MessageBoxNotice("str_recursiondrop_54", index);
                            return false;
                        }
                    }
                    else
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_35", index);
                        return false;
                    }
                }
                else
                {
                    int weight = 0;
                    if (int.TryParse(rate.Text.Trim(), out weight))
                    {
                        if (weight < 1)
                        {
                            Util.Util.MessageBoxNotice("str_recursiondrop_55", index);
                            return false;
                        }
                    }
                    else
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_35", index);
                        return false;
                    }
                    droprate = (double)weight;
                }

                int itemcount = -1;
                if (int.TryParse(count.Text.Trim(), out itemcount))
                {
                    if (isprecious.SelectedIndex == 0 || isprecious.SelectedIndex == 1)
                    {
                        usercontrol.RecursionDrop.DropItem di = new usercontrol.RecursionDrop.DropItem();
                        di.mDropType = td.DropType;
                        di.DropType = td.DropTypeName;
                        di.ItemId = dropitemid;
                        if (td.DropType == (int)EDropItemType.EDI_Item)
                        {
                            if (mItemList.ContainsKey(dropitemid) == false)
                            {
                                Util.Util.MessageBoxNotice("str_recursiondrop_38", 1);
                                return false;
                            }
                            di.ItemName = mItemList[dropitemid];

                            if (itemcount <= 0)
                            {
                                Util.Util.MessageBoxNotice("str_recursiondrop_39", 1);
                                return false;
                            }
                        }
                        else
                        {
                            di.ItemName = "";
                        }
                        di.Count = itemcount;
                        di.DropVal = droprate;
                        di.IsPrecious = isprecious.SelectedIndex == 0;
                        di.StrPrecious = di.IsPrecious ? Util.Util.GetDictionary("str_recursiondrop_21") : Util.Util.GetDictionary("str_recursiondrop_22");

                        dropList.Add(di);
                    }
                    else
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_37", index);
                        return false;
                    }
                }
                else
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_36", index);
                    return false;
                }

            }
            else
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_34", index);
                return false;
            }
            return true;
        }

        private void BT_OK_Click(object sender, RoutedEventArgs e)
        {
            if (mOnOKClick == null)
            {
                return;
            }
            List<usercontrol.RecursionDrop.DropItem> dropList = new List<usercontrol.RecursionDrop.DropItem>();
            if (CB_DropType1.SelectedItem != null)
            {
                DropTypeData dta = CB_DropType1.SelectedItem as DropTypeData;
                if (dta == null)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_40", 1);
                    return;
                }
                if (GenerateDropList(dropList, dta, TB_ItemId1, TB_DropRate1, TB_Count1, CB_Precious1, 1) == false)
                {
                    return;
                }
            }
            if (CB_DropType2.SelectedItem != null)
            {
                DropTypeData dta = CB_DropType2.SelectedItem as DropTypeData;
                if (dta == null)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_40", 2);
                    return;
                }
                if (GenerateDropList(dropList, dta, TB_ItemId2, TB_DropRate2, TB_Count2, CB_Precious2, 2) == false)
                {
                    return;
                }
            }
            if (CB_DropType3.SelectedItem != null)
            {
                DropTypeData dta = CB_DropType3.SelectedItem as DropTypeData;
                if (dta == null)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_40", 3);
                    return;
                }
                if (GenerateDropList(dropList, dta, TB_ItemId3, TB_DropRate3, TB_Count3, CB_Precious3, 3) == false)
                {
                    return;
                }
            }
            if (CB_DropType4.SelectedItem != null)
            {
                DropTypeData dta = CB_DropType4.SelectedItem as DropTypeData;
                if (dta == null)
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_40", 4);
                    return;
                }
                if (GenerateDropList(dropList, dta, TB_ItemId4, TB_DropRate4, TB_Count4, CB_Precious4, 4) == false)
                {
                    return;
                }
            }
            mOnOKClick(dropList);
            
            Close();
        }

        private void CB_DropType1_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType1.SelectedItem as DropTypeData;
            if (dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                TB_InputName1.Text = Util.Util.GetDictionary("str_recursiondrop_13");
                TB_InputCount1.Text = Util.Util.GetDictionary("str_recursiondrop_18");
                TB_Count1.Text = "";
                TB_Count1.IsEnabled = true;
                ShowItemName(TB_ItemName1, TB_ItemId1);
            }
            else if (dtd.DropType == (int)EDropItemType.EDI_Drop)
            {
                TB_InputName1.Text = Util.Util.GetDictionary("str_recursiondrop_14");
                TB_InputCount1.Text = Util.Util.GetDictionary("str_recursiondrop_19");
                TB_Count1.Text = "1";
                TB_Count1.IsEnabled = false;
                TB_ItemName1.Text = "";
            }
            else
            {
                TB_InputName1.Text = "";
                TB_InputCount1.Text = "";
                TB_Count1.Text = "";
                TB_Count1.IsEnabled = true;
                TB_ItemName1.Text = "";
            }
        }

        private void CB_DropType2_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType2.SelectedItem as DropTypeData;
            if (dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                TB_InputName2.Text = Util.Util.GetDictionary("str_recursiondrop_13");
                TB_InputCount2.Text = Util.Util.GetDictionary("str_recursiondrop_18");
                TB_Count2.Text = "";
                TB_Count2.IsEnabled = true;
                ShowItemName(TB_ItemName2, TB_ItemId2);
            }
            else if (dtd.DropType == (int)EDropItemType.EDI_Drop)
            {
                TB_InputName2.Text = Util.Util.GetDictionary("str_recursiondrop_14");
                TB_InputCount2.Text = Util.Util.GetDictionary("str_recursiondrop_19");
                TB_Count2.Text = "1";
                TB_Count2.IsEnabled = false;
                TB_ItemName2.Text = "";
            }
            else
            {
                TB_InputName2.Text = "";
                TB_InputCount2.Text = "";
                TB_Count2.Text = "";
                TB_Count2.IsEnabled = true;
                TB_ItemName2.Text = "";
            }
        }

        private void CB_DropType3_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType3.SelectedItem as DropTypeData;
            if (dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                TB_InputName3.Text = Util.Util.GetDictionary("str_recursiondrop_13");
                TB_InputCount3.Text = Util.Util.GetDictionary("str_recursiondrop_18");
                TB_Count3.Text = "";
                TB_Count3.IsEnabled = true;
                ShowItemName(TB_ItemName3, TB_ItemId3);
            }
            else if (dtd.DropType == (int)EDropItemType.EDI_Drop)
            {
                TB_InputName3.Text = Util.Util.GetDictionary("str_recursiondrop_14");
                TB_InputCount3.Text = Util.Util.GetDictionary("str_recursiondrop_19");
                TB_Count3.Text = "1";
                TB_Count3.IsEnabled = false;
                TB_ItemName3.Text = "";
            }
            else
            {
                TB_InputName3.Text = "";
                TB_InputCount3.Text = "";
                TB_Count3.Text = "";
                TB_Count3.IsEnabled = true;
                TB_ItemName3.Text = "";
            }
        }

        private void CB_DropType4_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            DropTypeData dtd = CB_DropType4.SelectedItem as DropTypeData;
            if (dtd.DropType == (int)EDropItemType.EDI_Item)
            {
                TB_InputName4.Text = Util.Util.GetDictionary("str_recursiondrop_13");
                TB_InputCount4.Text = Util.Util.GetDictionary("str_recursiondrop_18");
                TB_Count4.Text = "";
                TB_Count4.IsEnabled = true;
                ShowItemName(TB_ItemName4, TB_ItemId4);
            }
            else if (dtd.DropType == (int)EDropItemType.EDI_Drop)
            {
                TB_InputName4.Text = Util.Util.GetDictionary("str_recursiondrop_14");
                TB_InputCount4.Text = Util.Util.GetDictionary("str_recursiondrop_19");
                TB_Count4.Text = "1";
                TB_Count4.IsEnabled = false;
                TB_ItemName4.Text = "";
            }
            else
            {
                TB_InputName4.Text = "";
                TB_InputCount4.Text = "";
                TB_Count4.Text = "";
                TB_Count4.IsEnabled = true;
                TB_ItemName4.Text = "";
            }
        }


        public class ItemSearch: INotifyPropertyChanged
        {
            public int ItemId { get; set; }
            public string ItemName { get; set; }

            protected internal virtual void OnPropertyChanged(string propertyName)
            {
                if (PropertyChanged != null)
                {
                    PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
                }
            }
            public event PropertyChangedEventHandler PropertyChanged;
        }
        private ObservableCollection<ItemSearch> mItemSearchList = new ObservableCollection<ItemSearch>();

        private void Bt_SearchItem_Click(object sender, RoutedEventArgs e)
        {
            mItemSearchList.Clear();

            string str_key = TB_ItemIdInput.Text.Trim();
            if (string.IsNullOrEmpty(str_key))
            {
                Util.Util.MessageBoxNotice("str_recursiondrop_121");
                return;
            }
            
            foreach(var pair in mItemList)
            {
                if (pair.Value.Contains(str_key))
                {
                    ItemSearch item = new ItemSearch();
                    item.ItemId = pair.Key;
                    item.ItemName = pair.Value;
                    mItemSearchList.Add(item);
                }
            }
        }

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {
            ItemSearch item = Lv_ItemList.SelectedItem as ItemSearch;
            if (item != null)
            {
                Clipboard.SetText(item.ItemId.ToString());
            }
        }
    }
}
