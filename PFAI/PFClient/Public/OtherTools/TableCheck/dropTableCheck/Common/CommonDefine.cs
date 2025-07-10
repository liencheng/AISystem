using System.ComponentModel;

namespace GlobalDef
{
    enum ERandomType
    {
        ER_Invalid = 0,     // 无效的-1
        ER_Rate,            // 概率随机
        ER_Weight,          // 权重随机
    }

    enum EDropItemType
    {
        EDI_Item = 1,       // 掉落物品
        EDI_Drop,       // 掉落子包
    }

    public class DropTypeData : INotifyPropertyChanged
    {
        public int DropType { get; set; }
        private string mDropName = "";
        public string DropTypeName 
        { 
            get { return mDropName; } 
            set
            {
                mDropName = value;
                if (PropertyChanged != null)
                {
                    PropertyChanged(this, new PropertyChangedEventArgs("DropTypeName"));
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
}