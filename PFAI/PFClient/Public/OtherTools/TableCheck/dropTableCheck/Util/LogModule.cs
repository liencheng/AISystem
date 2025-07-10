using System;
using System.IO;

namespace Module.Log
{
    class LogModule
    {
        enum E_LOGCHANNEL
        {
            DEBUG = 0,
            WARNNING = 1,
            ERROR = 2,
        }

        private static readonly string[] logname = { "debug.log", "warnning.log", "error.log" };

        public static void Init()
        {
            File.AppendAllText(logname[(int)E_LOGCHANNEL.DEBUG], "");
            File.AppendAllText(logname[(int)E_LOGCHANNEL.WARNNING], "");
            File.AppendAllText(logname[(int)E_LOGCHANNEL.ERROR], "");
        }

        public static void ErrorLog(string msg)
        {
            WriteLog(msg, E_LOGCHANNEL.ERROR);
        }

        private static void WriteLog(string msg, E_LOGCHANNEL e)
        {
            string log_name = AppDomain.CurrentDomain.BaseDirectory.ToString() + logname[(int)e];
            string finstr = string.Format("{0} ({1})\r\n", msg, DateTime.Now.ToString());
            File.AppendAllText(log_name, finstr);
        }

        public static void DebugLog(string msg)
        {
            WriteLog(msg, E_LOGCHANNEL.DEBUG);
        }

    }
}
