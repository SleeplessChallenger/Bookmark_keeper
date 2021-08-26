import sqlite3


class DBManager:
	'''
	I've moved .cursor() to `_execute`
	as being present in `__init__`
	triggers errors
	'''
	def __init__(self, path):
		self.db = sqlite3.connect(path)

	def __del__(self):
		self.db.close()

	def _execute(self, data: str, values=None):
		with self.db:
			conn = self.db.cursor()
			conn.execute(data, values or [])
			return conn

	def create_table(self, table_name, data):
		data = [f"{col} {type_}" for col, type_ in data.items()]
		statement = f'''CREATE TABLE IF NOT EXISTS {table_name}
({', '.join(data)});'''
		self._execute(statement)

	def insert_data(self, table_name, values=None):
		placeholders = ', '.join('?' * len(values))
		# as we need string representation, use `join`
		columns = ', '.join(values.keys())
		data = list(values.values())

		statement = f'''INSERT INTO {table_name} ({columns})
VALUES ({placeholders});'''

		self._execute(statement, data)

	def delete_data(self, table_name, values):
		placeholders = [f'{col}=?' for col in values.keys()]
		# if there are multiple criteria -> `AND` them
		# else keep string without AND
		criteria = ' AND '.join(placeholders)
		data = list(values.values())
		statement = f'''DELETE FROM {table_name}
WHERE {criteria}'''
		self._execute(statement, data)

	def select_data(self, table_name, criteria=None, order_by=None):
		criteria = criteria or {}
		statement = f'''SELECT * FROM {table_name}'''

		if criteria:
			placeholders = [f'{col} = ?' for col in criteria.keys()]
			# # if there are multiple criteria -> `AND` them
			# else keep string without AND
			optional_criteria = ' AND '.join(placeholders)
			statement += f" WHERE {optional_criteria}"

		if order_by:
			statement += f" ORDER BY {order_by}"

		return self._execute(
			statement,
			list(criteria.values()),
		)

	def update_data(self, table_name, criteria, data):
		placeholders = [f"{col} = ?" for col in criteria.keys()]
		final_criteria = ' AND '.join(placeholders)

		new_data = ', '.join(f"{col} = ?" for col in data.keys())

		values = list(data.values()) + list(criteria.values())

		statement = f'''UPDATE {table_name} SET {new_data}
WHERE {final_criteria}'''
		
		self._execute(statement, values)
