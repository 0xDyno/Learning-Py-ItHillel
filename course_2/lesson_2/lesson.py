import os
import sqlite3


def execute_query(query_sql: str) -> list:
	db_path = os.path.join(os.getcwd(), "chinook.db")
	connection = sqlite3.connect(db_path)
	res = connection.cursor().execute(query_sql).fetchall()
	connection.close()
	return res