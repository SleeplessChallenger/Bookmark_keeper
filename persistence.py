from models import DBManager
from abc import ABC, abstractmethod


class PersistenceLayer(ABC):
	@abstractmethod
	def create(self, data):
		raise NotImplementedError("Method isn't realized!")

	@abstractmethod
	def list(self, order_by=None):
		raise NotImplementedError("Method isn't realized!")

	@abstractmethod
	def edit(self, c_id, edit_data):
		raise NotImplementedError("Method isn't realized!")

	@abstractmethod
	def delete(self, c_id):
		raise NotImplementedError("Method isn't realized!")


class BookmarkDB(PersistenceLayer):
	def __init__(self):
		self.t_name = 'bookmarks'
		self.db = DBManager('bookmarks.db')

		self.db.create_table(
			self.t_name,
			{
				'id': 'integer primary key autoincrement',
				'title': 'text not null',
				'url': 'text not null',
				'notes': 'text',
				'date_added': 'text not null'
			})

	def create(self, data):
		self.db.insert_data(self.t_name, data)

	def list(self, order_by=None):
		return self.db.select_data(self.t_name, order_by=order_by).fetchall()

	def edit(self, c_id, edit_data):
		self.db.update_data(self.t_name, c_id, edit_data)

	def delete(self, c_id):
		self.db.delete_data(self.t_name, c_id)
