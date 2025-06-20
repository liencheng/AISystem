#include <cstdint>
#include <ctime>
/*
todo:
	Signal的设计目的：用于通知AI行为，如：打断，切换状态等
	当前涉及的思路并不好，先不做处理后续添加。Signal应该是一个全局的概念，所有AI都可以发送和接收Signal。然后直接影响Goal，有Goal来驱动Behavior.
    现在Signal和Behaviro绑定了，感觉不是一个很好的设计。
	策划真正使用的时候，可以再某个时间帧上发送一个Signal或者由玩家发送一个Signal, 用于通知队友立即执行某个行为。
   

    同时再增加一个BehaviroTrigger。
	BehaviorTrigger和Behavior一一对应，用于通知AIPolicy立即执行某个行为。
*/

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