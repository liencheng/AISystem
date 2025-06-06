#pragma once

#include "sol_table_file.h"


namespace solar
{
	template <typename T>
	class table_uniqueid 
	{
		public:
			table_uniqueid() {}
			T* get_record_by_id(int id) { return nullptr; }
			T* get_record_by_index(int index) { return nullptr; }
			int get_record_count() { return 0; }

		public:
			void load_from_file(const std::string& file) 
			{
				solar::table_file tf;
				tf.load(file);
				m_record_count = tf.get_record_count();
				for (int i = 0; i < m_record_count; ++i) {
					T* record = new T();
					tf.read_record(*record, i);
					m_records.push_back(*record);
				}

			}

		private:
			std::vector<T> m_records;
			int m_record_count;
	};
}



#define TABLE_ENTITY ( NAME ) gTable_##NAME 
#define TABLE_ENTITY_DECL ( NAME ) extern solar::table_uniqueid<NAME> TABLE_ENTITY ( NAME )
#define TABLE_ENTITY_IMPL ( NAME ) solar::table_uniqueid<NAME> TABLE_ENTITY( NAME )
#define TABLE_GET_BY_ID ( NAME ) TABLE_ENTITY(NAME).get_record_by_id 
#define TABLE_GET_BY_INDEX ( NAME ) TABLE_ENTITY( NAME ).get_record_by_index 
#define TABLE_GET_COUNT ( NAME ) TABLE_ENTITY( NAME ).get_record_count()
