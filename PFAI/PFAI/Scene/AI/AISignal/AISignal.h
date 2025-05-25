#include <cstdint>
#include <ctime>

enum class AISignalType
{
    SIGNAL_TYPE_UNKNOWN,
    SIGNAL_TYPE_MOVE,
    SIGNAL_TYPE_ATTACK,
    SIGNAL_TYPE_PATROL,
    SIGNAL_TYPE_FOLLOW,
    SIGNAL_TYPE_STOP,
};

class AISignal
{
    public:
        AISignal();
        ~AISignal();

        bool    isExpired() const;
        int32_t GetWeight() const{ return m_Weight; }

    private:
        int32_t         m_SenderObjId;
        time_t          m_ExpiredTime; 
        //signal 的权重大小从 100000 开始，用于区分优先级，数值越大越优先处理
        int32_t         m_Weight;
        AISignalType    m_type;
};