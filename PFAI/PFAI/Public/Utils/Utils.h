#include <string>
#include <vector>
#include <sstream>

namespace solar
{
    class StringUtils
    {
        //C++静态函数，用|分割字符串，并返回int32_t数组

        public:
        static std::vector<int32_t> SplitString(std::string str)
        {
            std::vector<int32_t> result;
            std::istringstream iss(str);
            std::string val;
            while (std::getline(iss, val, '|') && !val.empty())
            {
                result.push_back(std::stoi(val));
            }
            return result;
        }
    }
}