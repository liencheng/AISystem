#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <mutex>
#include <ctime>
#include <iomanip>
#include <sstream>

#define LOG_FATAL(message) utils::Logger::getInstance().log(utils::LogLevel::Fatal, __FILE__ ":" + std::to_string(__LINE__) + " - " + message)
#define LOG_ERROR(message) utils::Logger::getInstance().log(utils::LogLevel::Error, __FILE__ ":" + std::to_string(__LINE__) + " - " + message)
#define LOG_WARNING(message) utils::Logger::getInstance().log(utils::LogLevel::Warning, __FILE__ ":" + std::to_string(__LINE__) + " - " + message)
#define LOG_INFO(message) utils::Logger::getInstance().log(utils::LogLevel::Info, __FILE__ ":" + std::to_string(__LINE__) + " - " + message)

namespace utils {

    enum class LogLevel {
        Fatal,
        Error,
        Warning,
        Info
    };

    class Logger {
    public:
        static Logger& getInstance() {
            static Logger instance;
            return instance;
        }

        void setLogFile(const std::string& fileName) {
            std::lock_guard<std::mutex> lock(mutex_);
            if (logFile_.is_open()) {
                logFile_.close();
            }
            logFile_.open(fileName, std::ios::out | std::ios::app);
            if (!logFile_.is_open()) {
                std::cerr << "Failed to open log file: " << fileName << std::endl;
            }
        }

        void log(LogLevel level, const std::string& message) {
            std::lock_guard<std::mutex> lock(mutex_);
            if (!logFile_.is_open()) {
                std::cerr << "Log file is not open!" << std::endl;
                return;
            }

            logFile_ << getCurrentTime() << " [" << logLevelToString(level) << "] " << message << std::endl;
        }

    private:
        Logger() = default;
        ~Logger() {
            if (logFile_.is_open()) {
                logFile_.close();
            }
        }

        Logger(const Logger&) = delete;
        Logger& operator=(const Logger&) = delete;

        std::string getCurrentTime() {
            auto now = std::time(nullptr);
            std::tm tm;
#ifdef _WIN32
            localtime_s(&tm, &now);
#else
            localtime_r(&now, &tm);
#endif
            std::ostringstream oss;
            oss << std::put_time(&tm, "%Y-%m-%d %H:%M:%S");
            return oss.str();
        }

        std::string logLevelToString(LogLevel level) {
            switch (level) {
                case LogLevel::Fatal: return "Fatal";
                case LogLevel::Error: return "Error";
                case LogLevel::Warning: return "Warning";
                case LogLevel::Info: return "Info";
                default: return "Unknown";
            }
        }

        std::ofstream logFile_;
        std::mutex mutex_;
    };

} // namespace utils
