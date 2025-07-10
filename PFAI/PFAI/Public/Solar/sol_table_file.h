#pragma once
#include <vector>
#include <filesystem>
#include <fstream>
#include <string>
#include <strstream>
#include <iostream>
#include <sstream>
#include "sol_assert.h"

#define TABLE_FILE_VERSION 1
#define TABLE_FILE_TYPE_ROW 1    //字段类型
#define TABLE_FILE_DATA_ROW 4    //数据行
namespace solar {


	class table_filed_type
	{
		public:
			enum 
			{
				T_INT8 = 0,
				T_INT16,
				T_INT,
				T_INT64,
				T_FLOAT,
				T_DOUBLE,
				T_BOOL,
				T_STRING,
				T_VECTOR2,
				T_VECTOR3,
			};
	};

	class table_string
	{

	public:
		table_string()
		{
			m_pstr = m_str.c_str();
		}
		~table_string() 
		{
			if (m_pstr != m_str.c_str())
			{
				delete[] m_pstr;
			}
		}
		table_string(const table_string& other) = delete;
		table_string& operator=(const table_string& other) = delete;
		table_string& operator=(const std::string& str)
		{
			if (m_pstr != m_str.c_str())
			{
				delete[] m_pstr;
			}
			m_str = str;
			m_pstr = m_str.c_str();
			return *this;
		}
		const char* c_text() const { return m_pstr; }

	private:
		std::string m_str;
		const char* m_pstr;


	};

	class table_file 
	{
	public:
		using table_line = std::vector<std::string>;

	public:
		table_file() : m_file_path(""), m_table_lines(), m_table_filed_vec() {}
		explicit table_file(const std::string& file, bool multiplyid = false)
		{
		}
		~table_file() {};

		int32_t get_record_count() const
		{
			return static_cast<int32_t>(m_table_lines.size());
		}

		int32_t get_filed_count() const
		{
			return m_table_filed_vec.size();
		}

		const std::string& get_table_string(int32_t index, int32_t filed_num) const
		{
			return m_table_lines[index][filed_num];
		}

		void read_filed_type(const std::string& filed_type_line)
		{
			std::stringstream ss(filed_type_line);
			std::string filed_type;
			while (ss >> filed_type) {
				if (filed_type == "INT8"){ m_table_filed_vec.push_back(table_filed_type::T_INT8);}
				if (filed_type == "INT16"){	m_table_filed_vec.push_back(table_filed_type::T_INT16);}
				if (filed_type == "INT"){	m_table_filed_vec.push_back(table_filed_type::T_INT);}
				if (filed_type == "INT64"){	m_table_filed_vec.push_back(table_filed_type::T_INT64);}
				if (filed_type == "FLOAT"){	m_table_filed_vec.push_back(table_filed_type::T_FLOAT);}
				if (filed_type == "DOUBLE"){	m_table_filed_vec.push_back(table_filed_type::T_DOUBLE);}
				if(filed_type == "BOOL"){	m_table_filed_vec.push_back(table_filed_type::T_BOOL);}
				if (filed_type == "STRING") { m_table_filed_vec.push_back(table_filed_type::T_STRING); }
				if (filed_type == "VECTOR2") { m_table_filed_vec.push_back(table_filed_type::T_VECTOR2); }
				if (filed_type == "VECTOR3") { m_table_filed_vec.push_back(table_filed_type::T_VECTOR3); }
				
			}
		}

		void load(const std::string& file_path)
		{
			m_file_path = file_path;
			m_table_lines.clear();
			m_table_filed_vec.clear();

			std::string full_path = m_file_path;
			std::ifstream file(full_path);

			if (!file.is_open()) {
				std::cerr << "Failed to open file: " << full_path << std::endl;
				return;
			}

			std::string line;
			int32_t line_num = 0;
			int32_t data_row = 0;
			while (std::getline(file, line)) {

				if (line_num == TABLE_FILE_TYPE_ROW)
				{
					++line_num;
					read_filed_type(line);
					continue;
				}

				if (line_num < TABLE_FILE_DATA_ROW)
				{
					++line_num;
					continue;
				}
				table_line line_vec;
				if (!line.empty()) {
					std::stringstream ss(line);
					std::string value;
					while (std::getline(ss, value, '\t')) {
						line_vec.push_back(value);
					}
					if (!line_vec.empty()) {
						m_table_lines.push_back(line_vec);
					}
				}
			}

		}

	public:
		void read(int8_t& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stoi(val);
		}
		void read(int16_t& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stoi(val);
		}
		void read(int32_t& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stoi(val);
		}
		void read(int64_t& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stoll(val);
		}
		void read(float& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stof(val);
		}
		void read(double& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stod(val);
		}
		void read(bool& value, int32_t index, int32_t filed_num) const
		{
			std::string val = get_table_string(index, filed_num);
			value = std::stoi(val) != 0;
		}
		void read(std::string& value, int32_t index, int32_t filed_num) const
		{
			value = get_table_string(index, filed_num);
		}

		void read(table_string& value, int32_t index, int32_t filed_num) const
		{
			value = get_table_string(index, filed_num);
		}

	private:
		std::string m_file_path;
		std::string m_file_name;

		std::vector<int32_t> m_table_filed_vec;
		std::vector<table_line> m_table_lines;

	};
};



