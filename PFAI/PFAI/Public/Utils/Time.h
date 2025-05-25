#include <iostream>
#include <chrono>

class TimeHelper {
public:
    static time_t getCurrentTimestamp() {
        auto now = std::chrono::system_clock::now();
        auto in_time_t = std::chrono::system_clock::to_time_t(now);
        return (in_time_t);
    }
    // 其他辅助函数...
};
