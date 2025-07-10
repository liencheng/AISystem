using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.IO;
using System.Text;
using System.Data;

namespace TableAnalyzer
{
    public enum CODE_SEGMENT_TYPE
    {
        COMMON,
        LOOP,
        TEMPLATE,
        SQLREPLACE,
    };

    public class CodeSegment
    {
        public CODE_SEGMENT_TYPE m_Type;
        public string m_Str;
        public List<string> m_Param;

        public CodeSegment()
        {
            m_Type = CODE_SEGMENT_TYPE.COMMON;
            m_Str = "";
            m_Param = new List<string>();
        }
    };

    public class AnalyzerCore
    {
        public static string TABLE_CLIENT_PATH = "../../../../../ClientTables/";
        public static string TABLE_SERVER_PATH = "../../../../../ServerTables/";
        public static string TABLE_PUBLIC_PATH = "../../../../../PublicTables/";
        public static string TABLE_PRESET_PATH = "../../../PresetTable/";
        public static string TABLE_TMP_PATH = "../../../TmpTable";
        public static string CMD_FILE_PATH = "../../../SQLScript/";

        private static string SQL_VERSION_COMPLEX = "--[This is a complex sql format Version:";
        private static string SQL_SEGMENT_LOOP = "--[LOOPTABLE";
        private static string SQL_SEGMENT_TEMPLATE = "--[LOOPTEMPLATE";
        private static string SQL_SEGMENT_SQLREPLACE = "--[REPLACESQLRESULT";
        private static string SQL_SEGMENT_END = "]--";

        SQLiteConnection connection = null;

        public void Init()
        {
            connection = new SQLiteConnection("Data Source=:memory:");
            connection.Open();
            if (Directory.Exists(Path.GetFullPath(TABLE_TMP_PATH)))
            {
                Directory.Delete(Path.GetFullPath(TABLE_TMP_PATH), true);
            }
            Directory.CreateDirectory(Path.GetFullPath(TABLE_TMP_PATH));
        }

        public bool ReadTableToDB(string tableName)
        {
            string tablePath = Path.GetFullPath(TABLE_PUBLIC_PATH + tableName + ".txt");
            if (File.Exists(tablePath) == false)
            {
                tablePath = Path.GetFullPath(TABLE_CLIENT_PATH + tableName + ".txt");
            }
            if (File.Exists(tablePath) == false)
            {
                tablePath = Path.GetFullPath(TABLE_SERVER_PATH + tableName + ".txt");
            }
            if (File.Exists(tablePath) == false)
            {
                tablePath = Path.GetFullPath(TABLE_PRESET_PATH + tableName + ".txt");
            }
            if (File.Exists(tablePath) == false)
            {
                return false;
            }

            File.Copy(tablePath, Path.GetFullPath(TABLE_TMP_PATH + "/" + tableName + ".txt"));
            tablePath = Path.GetFullPath(TABLE_TMP_PATH + "/" + tableName + ".txt");

            FileStream fs = File.OpenRead(tablePath);
            StreamReader sr = new StreamReader(fs, Encoding.GetEncoding("GB2312"));
            string[] columnName = { };
            string[] columnTypeStr = { };
            string[] columnType = { };
            int lineId = 0;
            while (!sr.EndOfStream)
            {
                string line = sr.ReadLine();
                lineId++;
                if (lineId == 1)
                {
                    //表格列
                    columnName = line.Split('\t');
                }
                else if (lineId == 2)
                {
                    //数据类型
                    columnTypeStr = line.Split('\t');
                    columnType = new string[columnTypeStr.Length];
                    for (int idx = 0; idx < columnTypeStr.Length; idx++)
                    {
                        if (columnTypeStr[idx] == "INT")
                        {
                            columnType[idx] = "INTEGER";
                        }
                        else if (columnTypeStr[idx] == "FLOAT")
                        {
                            columnType[idx] = "REAL";
                        }
                        else
                        {
                            columnType[idx] = "TEXT";
                        }
                    }
                    //创建表格
                    string colDefineStr = "";
                    if (columnName.Length != columnType.Length)
                    {
                        return false;
                    }
                    for (int idx = 0; idx < columnName.Length; idx++)
                    {
                        colDefineStr += columnName[idx] + " ";
                        colDefineStr += columnType[idx];
                        if (idx != columnName.Length - 1)
                        {
                            colDefineStr += ",";
                        }
                    }
                    string sqlCreateTable = "create table " + tableName + " (" + colDefineStr + ");";
                    SQLiteCommand cmd = new SQLiteCommand(sqlCreateTable, connection);
                    cmd.ExecuteNonQuery();
                }
                else if (lineId <= 4)
                {
                    continue;
                }
                else
                {
                    if (line.StartsWith("#")) continue;
                    string[] values = line.Split('\t');
                    //每一行的数据
                    {
                        string sqlInsert = "insert into " + tableName + " values(";
                        for (int idx = 0; idx < values.Length; idx++)
                        {
                            sqlInsert += "'" + values[idx].Replace('\'', '#') + "'";
                            if (idx != values.Length - 1)
                            {
                                sqlInsert += ",";
                            }
                        }
                        sqlInsert += ");";
                        SQLiteCommand cmd = new SQLiteCommand(sqlInsert, connection);
                        cmd.ExecuteNonQuery();
                    }
                }
            }

            sr.Close();
            fs.Close();

            return true;
        }

        public int ExecuteSQLCommand(string cmdFileName)
        {
            int ret = 0;
            string filePath = Path.GetFullPath(CMD_FILE_PATH + cmdFileName + ".sql");
            if (File.Exists(filePath) == false)
            {
                return -1;
            }
            string cmdStr = File.ReadAllText(filePath);
            List<CodeSegment> segments = new List<CodeSegment>();
            CodeSegment curSegment = new CodeSegment();
            string[] lines = cmdStr.Split('\n');
            for (int idx = 0; idx < lines.Length; idx++)
            {
                //版本描述符，跳过
                if (lines[idx].Contains(SQL_VERSION_COMPLEX))
                {
                    continue;
                }

                //循环开始
                if (lines[idx].StartsWith(SQL_SEGMENT_LOOP) && !lines[idx].Contains(SQL_SEGMENT_LOOP + SQL_SEGMENT_END))
                {
                    if (curSegment.m_Str.Length > 0)
                    {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.LOOP;
                        //参数1为待循环的表格
                        curSegment.m_Param.Add(lines[idx].Substring(SQL_SEGMENT_LOOP.Length, lines[idx].IndexOf(SQL_SEGMENT_END) - SQL_SEGMENT_LOOP.Length).Trim());
                    }
                    continue;
                }

                //循环结束
                if (lines[idx].Contains(SQL_SEGMENT_LOOP + SQL_SEGMENT_END))
                {
                    if (curSegment.m_Str.Length > 0)
                    {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.COMMON;
                    }
                    continue;
                }

                // 模板开始
                if (lines[idx].StartsWith(SQL_SEGMENT_TEMPLATE) && !lines[idx].Contains(SQL_SEGMENT_TEMPLATE + SQL_SEGMENT_END))
                {
                    if (curSegment.m_Str.Length > 0) {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.TEMPLATE;
                        //参数1为待循环的表格
                        curSegment.m_Param.Add(lines[idx].Substring(SQL_SEGMENT_TEMPLATE.Length, lines[idx].IndexOf(SQL_SEGMENT_END) - SQL_SEGMENT_TEMPLATE.Length).Trim());
                    }
                    continue;
                }

                // 模板结束
                if (lines[idx].Contains(SQL_SEGMENT_TEMPLATE + SQL_SEGMENT_END)) {
                    if (curSegment.m_Str.Length > 0) {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.COMMON;
                    }
                    continue;
                }

                // sql结果替换开始
                if (lines[idx].StartsWith(SQL_SEGMENT_SQLREPLACE) && !lines[idx].Contains(SQL_SEGMENT_SQLREPLACE + SQL_SEGMENT_END)) {
                    if (curSegment.m_Str.Length > 0) {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.SQLREPLACE;
                        //参数1为待循环的表格
                        curSegment.m_Param.Add(lines[idx].Substring(SQL_SEGMENT_SQLREPLACE.Length, lines[idx].IndexOf(SQL_SEGMENT_END) - SQL_SEGMENT_SQLREPLACE.Length).Trim());
                    }
                    continue;
                }

                // sql结果替换结束
                if (lines[idx].Contains(SQL_SEGMENT_SQLREPLACE + SQL_SEGMENT_END)) {
                    if (curSegment.m_Str.Length > 0) {
                        segments.Add(curSegment);
                        curSegment = new CodeSegment();
                        curSegment.m_Type = CODE_SEGMENT_TYPE.COMMON;
                    }
                    continue;
                }

                curSegment.m_Str += lines[idx] + "\n";
            }
            //内容结束
            if (curSegment.m_Str.Length > 0)
            {
                segments.Add(curSegment);
            }

            for (int idx = 0; idx < segments.Count; idx++)
            {
                if (segments[idx].m_Type == CODE_SEGMENT_TYPE.COMMON)
                {
                    //普通代码段直接执行
                    SQLiteCommand cmd = new SQLiteCommand(segments[idx].m_Str, connection);
                    ret = cmd.ExecuteNonQuery();
                }
                else if (segments[idx].m_Type == CODE_SEGMENT_TYPE.LOOP)
                {
                    //循环代码段，先取出要循环的表格
                    string sqlSelect = "select * from " + segments[idx].m_Param[0];
                    SQLiteCommand cmdSelect = new SQLiteCommand(sqlSelect, connection);
                    SQLiteDataReader reader = cmdSelect.ExecuteReader();
                    //遍历表格
                    int iterationIdx = 0;
                    //创建循环参数表
                    string colDefineStr = "IterationIndex integer,";
                    for (int colIdx = 0; colIdx < reader.FieldCount; colIdx++)
                    {
                        colDefineStr += reader.GetName(colIdx) + " ";
                        if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int32"))
                        {
                            colDefineStr += "integer";
                        }
                        else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int64"))
                        {
                            colDefineStr += "integer";
                        }
                        else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Single"))
                        {
                            colDefineStr += "number";
                        }
                        else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Double"))
                        {
                            colDefineStr += "number";
                        }
                        else
                        {
                            colDefineStr += "text";
                        }

                        if (colIdx != reader.FieldCount - 1)
                        {
                            colDefineStr += ",";
                        }
                    }
                    string sqlCreateTable = "drop table if exists t_iteration_param; \n create table t_iteration_param " + " (" + colDefineStr + ");";
                    SQLiteCommand makeParamCmd = new SQLiteCommand(sqlCreateTable, connection);
                    makeParamCmd.ExecuteNonQuery();
                    while (reader.Read())
                    {
                        {
                            //填充循环参数表
                            string colValueStr = iterationIdx.ToString();
                            iterationIdx++;
                            if (reader.FieldCount > 0)
                            {
                                colValueStr += ",";
                            }
                            for (int colIdx = 0; colIdx < reader.FieldCount; colIdx++)
                            {
                                if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int32"))
                                {
                                    colValueStr += reader.GetFieldValue<int>(colIdx).ToString();
                                }
                                else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int64"))
                                {
                                    colValueStr += reader.GetFieldValue<long>(colIdx).ToString();
                                }
                                else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Single"))
                                {
                                    colValueStr += reader.GetFieldValue<float>(colIdx).ToString();
                                }
                                else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Double"))
                                {
                                    colValueStr += reader.GetFieldValue<double>(colIdx).ToString();
                                }
                                else
                                {
                                    colValueStr += "'" + reader.GetFieldValue<string>(colIdx) + "'";
                                }
                                if (colIdx != reader.FieldCount - 1)
                                {
                                    colValueStr += ",";
                                }
                            }
                            string sqlInsert = "delete from t_iteration_param; \n insert into t_iteration_param values(" + colValueStr + ");";
                            SQLiteCommand insertParamCmd = new SQLiteCommand(sqlInsert, connection);
                            insertParamCmd.ExecuteNonQuery();

                            //执行循环代码段
                            SQLiteCommand cmd = new SQLiteCommand(segments[idx].m_Str, connection);
                            ret = cmd.ExecuteNonQuery();
                        }
                    }
                }
                else if (segments[idx].m_Type == CODE_SEGMENT_TYPE.TEMPLATE)
                {
                    // 获取参数
                    string[] paramArr = segments[idx].m_Param[0].Split(' ');
                    if (paramArr.Length < 2) {
                        continue;
                    }

                    string placeholderStr = paramArr[0];
                    int loopMax = 0;
                    int.TryParse(paramArr[1], out loopMax);
                    string commondStr = "";
                    for (int i = 0; i < loopMax; i++) {
                        string temp = segments[idx].m_Str;
                        commondStr += temp.Replace(placeholderStr, (i + 1).ToString());
                    }
                    //执行代码段
                    SQLiteCommand cmd = new SQLiteCommand(commondStr, connection);
                    ret = cmd.ExecuteNonQuery();
                } 
                else if (segments[idx].m_Type == CODE_SEGMENT_TYPE.SQLREPLACE) 
                {
                    // 获取参数
                    string[] paramArr = segments[idx].m_Param[0].Split('|');
                    if (paramArr.Length < 2) {
                        continue;
                    }

                    string placeholderStr = paramArr[0];
                    string sqlString = paramArr[1];
                    SQLiteCommand cmdSelect = new SQLiteCommand(sqlString, connection);
                    SQLiteDataReader reader = cmdSelect.ExecuteReader();
                    string commondStr = "";
                    string colValueStr = "";
                    while (reader.Read())
                    {
                        for (int colIdx = 0; colIdx < reader.FieldCount; colIdx++)
                        {
                            if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int32"))
                            {
                                colValueStr += reader.GetFieldValue<int>(colIdx).ToString();
                            }
                            else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Int64"))
                            {
                                colValueStr += reader.GetFieldValue<long>(colIdx).ToString();
                            }
                            else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Single"))
                            {
                                colValueStr += reader.GetFieldValue<float>(colIdx).ToString();
                            }
                            else if (reader.GetFieldType(colIdx) == System.Type.GetType("System.Double"))
                            {
                                colValueStr += reader.GetFieldValue<double>(colIdx).ToString();
                            }
                            else
                            {
                                colValueStr += "'" + reader.GetFieldValue<string>(colIdx);
                            }
                        }
                    }
                    string temp = segments[idx].m_Str;
                    commondStr += temp.Replace(placeholderStr, colValueStr);
                    //执行代码段
                    SQLiteCommand cmd = new SQLiteCommand(commondStr, connection);
                    ret = cmd.ExecuteNonQuery();
                }
            }

            return ret;
        }

        public void ShowResultTable()
        {
            string sqlSearch = "select * from " + "t_result";
            SQLiteCommand cmd = new SQLiteCommand(sqlSearch, connection);
            SQLiteDataReader reader = cmd.ExecuteReader();
            Console.WriteLine();
            while (reader.Read())
            {
                for (int idx = 0; idx < reader.FieldCount; idx++)
                {
                    Console.Write(Convert.ToString(reader.GetValue(idx)) + ",");
                }
                Console.WriteLine();
            }
        }

        public void SetParams(DataTable tab)
        {
            string sqlDrop = "drop table if exists t_param";
            SQLiteCommand cmd = new SQLiteCommand(sqlDrop, connection);
            cmd.ExecuteNonQuery();

            if (tab.Columns.Count <= 0)
            {
                return;
            }

            string colDefineStr = "";
            for (int idx = 0; idx < tab.Columns.Count; idx++)
            {
                colDefineStr += tab.Columns[idx].ColumnName + " ";
                if (tab.Columns[idx].DataType == System.Type.GetType("System.Int32"))
                {
                    colDefineStr += "integer";
                }
                else if (tab.Columns[idx].DataType == System.Type.GetType("System.Int64"))
                {
                    colDefineStr += "integer";
                }
                else if (tab.Columns[idx].DataType == System.Type.GetType("System.Single"))
                {
                    colDefineStr += "number";
                }
                else if (tab.Columns[idx].DataType == System.Type.GetType("System.Double"))
                {
                    colDefineStr += "number";
                }
                else
                {
                    colDefineStr += "text";
                }

                if (idx != tab.Columns.Count - 1)
                {
                    colDefineStr += ",";
                }
            }

            string sqlCreateTable = "create table t_param " + " (" + colDefineStr + ");";
            cmd = new SQLiteCommand(sqlCreateTable, connection);
            cmd.ExecuteNonQuery();

            for (int rowId = 0; rowId < tab.Rows.Count; rowId++)
            {
                string colValueStr = "";
                for (int idx = 0; idx < tab.Columns.Count; idx++)
                {
                    if (tab.Columns[idx].DataType == System.Type.GetType("System.String"))
                    {
                        colValueStr += "'" + tab.Rows[rowId][idx].ToString() + "'";
                    }
                    else
                    {
                        colValueStr += tab.Rows[rowId][idx].ToString();
                    }
                    
                    if (idx != tab.Columns.Count - 1)
                    {
                        colValueStr += ",";
                    }
                }

                string sqlInsert = "insert into t_param values(" + colValueStr + ");";
                cmd = new SQLiteCommand(sqlInsert, connection);
                cmd.ExecuteNonQuery();
            }
        }

        public DataSet GetResultTable()
        {
            string sqlSearch = "select * from t_result";
            SQLiteDataAdapter sda = new SQLiteDataAdapter(sqlSearch, connection);
            DataSet ret = new DataSet();
            sda.Fill(ret);

            return ret;
        }
    }
}
