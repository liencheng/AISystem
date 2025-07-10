using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;
using GlobalDef;

namespace TableCheck.Window
{
    /// <summary>
    /// DropModify.xaml 的交互逻辑
    /// </summary>
    public partial class DropModify : System.Windows.Window
    {
        public Dictionary<int, string> mItemList = null;
        public usercontrol.RecursionDrop.DropItem dropItem = null;
        public string StrRate = "";

        public delegate void OKModify(usercontrol.RecursionDrop.DropItem di);
        public OKModify mOnModify = null;

        private string mFillStr = "0.##########";

        public DropModify()
        {
            InitializeComponent();
        }

        public void InitData()
        {
            if (dropItem == null)
            {
                return;
            }
            CB_DropType.SelectedIndex = (dropItem.mDropType == (int)EDropItemType.EDI_Item || dropItem.mDropType == (int)EDropItemType.EDI_Drop) ? dropItem.mDropType : -1;
            TB_ItemId.Text = dropItem.ItemId.ToString();
            TB_InputRate.Text = StrRate;
            TB_DropRate.Text = dropItem.DropVal.ToString(mFillStr);
            TB_Count.Text = dropItem.Count.ToString();
            CB_Precious.SelectedIndex = dropItem.IsPrecious  ? 0 : 1;
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

        private void CB_DropType_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if (CB_DropType.SelectedIndex == (int)EDropItemType.EDI_Item)
            {
                TB_InputName.Text = Util.Util.GetDictionary("str_recursiondrop_13");
                TB_InputCount.Text = Util.Util.GetDictionary("str_recursiondrop_18");
                TB_Count.Text = "";
                TB_Count.IsEnabled = true;
                ShowItemName(TB_ItemName, TB_ItemId);
            }
            else if (CB_DropType.SelectedIndex == (int)EDropItemType.EDI_Drop)
            {
                TB_InputName.Text = Util.Util.GetDictionary("str_recursiondrop_14");
                TB_InputCount.Text = Util.Util.GetDictionary("str_recursiondrop_19");
                TB_Count.Text = "1";
                TB_Count.IsEnabled = false;
                TB_ItemName.Text = "";
            }
            else
            {
                TB_InputName.Text = "";
                TB_InputCount.Text = "";
                TB_Count.Text = "";
                TB_Count.IsEnabled = true;
                TB_ItemName.Text = "";
            }    
        }

        private void TB_ItemId_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (CB_DropType.SelectedIndex == (int)EDropItemType.EDI_Item)
            {
                ShowItemName(TB_ItemName, TB_ItemId);
            }
            else
            {
                TB_ItemName.Text = "";
            }
        }

        private void Bt_OKModify_Click(object sender, RoutedEventArgs e)
        {
            if (mOnModify != null)
            {
                dropItem.mDropType = CB_DropType.SelectedIndex == 0 ? -1 : CB_DropType.SelectedIndex;
                if (dropItem.mDropType == (int)EDropItemType.EDI_Item)
                {
                    dropItem.DropType = Util.Util.GetDictionary("str_recursiondrop_11");
                }
                else if (dropItem.mDropType == (int)EDropItemType.EDI_Drop)
                {
                    dropItem.DropType = Util.Util.GetDictionary("str_recursiondrop_12");
                }
                else
                {
                    dropItem.DropType = "";
                }
                int itemid = -1;
                if (int.TryParse(TB_ItemId.Text.Trim(), out itemid))
                {
                    if (itemid == -1)
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_46");
                        return;
                    }
                    double rateval = 0f;
                    if (double.TryParse(TB_DropRate.Text.Trim(), out rateval))
                    {
                        int count = -1;
                        if (int.TryParse(TB_Count.Text.Trim(), out count))
                        {
                            dropItem.ItemId = itemid;
                            if (dropItem.mDropType == (int)EDropItemType.EDI_Item)
                            {
                                if (mItemList.ContainsKey(itemid))
                                {
                                    dropItem.ItemName = mItemList[itemid];
                                }
                                else
                                {
                                    Util.Util.MessageBoxNotice("str_recursiondrop_49");
                                    return;
                                }
                            }
                            
                            dropItem.DropVal = rateval;
                            dropItem.Count = count;
                            dropItem.IsPrecious = CB_Precious.SelectedIndex == 0;
                            if (dropItem.IsPrecious)
                            {
                                dropItem.StrPrecious = Util.Util.GetDictionary("str_recursiondrop_21");
                            }
                            else
                            {
                                dropItem.StrPrecious = Util.Util.GetDictionary("str_recursiondrop_22");
                            }
                        }
                        else
                        {
                            Util.Util.MessageBoxNotice("str_recursiondrop_48");
                            return;
                        }
                    }
                    else
                    {
                        Util.Util.MessageBoxNotice("str_recursiondrop_47");
                        return;
                    }
                }
                else
                {
                    Util.Util.MessageBoxNotice("str_recursiondrop_46");
                    return;
                }

                mOnModify(dropItem);
            }
            Close();
        }
    }
}
