#include <cstdint>
#include <ctime>

enum class E_AISignalType
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
    E_AISignalType GetSignalType() const { return m_type; }
    int32_t GetSenderObjId() const { return m_SenderObjId; }
    time_t  GetExpiredTime() const { return m_ExpiredTime; }

    void SetSenderObjId(int32_t id) { m_SenderObjId = id; }
    void SetExpiredTime(time_t t) { m_ExpiredTime = t; }
    void SetWeight(int32_t weight) { m_Weight = weight; }
    void SetSignalType(E_AISignalType type) { m_type = type; }

private:
    int32_t         m_SenderObjId;
    time_t          m_ExpiredTime; 
    //signal 的权重大小从 100000 开始，用于区分优先级，数值越大越优先处理
    int32_t         m_Weight;
    E_AISignalType    m_type;
};