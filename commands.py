from persistence import BookmarkDB
from datetime import datetime
from sys import exit
import requests
from datetime import datetime
from abc import ABC, abstractmethod


storage = BookmarkDB()
'''
after adding abstract class
we need to make `execute()` similar in each class.
So, specifying `data` in every `execute()`
function is crucial and where it's not used
we'll place None.
PS: Actual `data` variable will be placed instead of
`bookmark_id` etc
'''


class Command(ABC):
	@abstractmethod
	def execute(self, data):
		raise NotImplementedError("Method isn't realized")


class AddBookmark(Command):
	def execute(self, data, timestamp=None):
		data['date_added'] = timestamp or datetime.utcnow().isoformat()
		storage.create(data)
		return True, None


class ListBookmarks(Command):
	def __init__(self, order_by='date_added'):
		self.order_by = order_by

	def execute(self, data=None):
		return True, storage.list(order_by=self.order_by)


class DeleteBookmark(Command):
	def execute(self, data):
		# data is a dict already
		storage.delete(data)
		return True, None


class QuitProgram(Command):
	def execute(self, data=None):
		exit()


class AddGitHub(Command):
	def _extract_info(self, repo):
		return {
			'title': repo['name'],
			'url': repo['html_url'],
			'notes': repo['description']
		}

	def execute(self, data):
		number_imported = 0
		username = data['username']
		url = f"https://api.github.com/users/{username}/starred"

		while url:
			response = requests.get(url,
				headers={'Accept': 'application/vnd.github.v3.star+json'})

			url = response.links.get('next', {}).get('url')

			for r in response.json():
				repo = r['repo']
				if data['timestamp']:
					timestamp = datetime.strptime(
                        repo['created_at'],
                        '%Y-%m-%dT%H:%M:%SZ')
				else:
					timestamp = None

				result = self._extract_info(repo)
				AddBookmark().execute(result, timestamp=timestamp)
				number_imported += 1

		return True, number_imported


class UpdateBookmark(Command):
	'''
	as in data we have nested dict,
	we must apply additional key()
	'''
	def execute(self, data):
		data_id  = data['id']
		data_update = data['new info']
		storage.edit(
			{'id': data['id']},
			 data['new info']
		)
		return True, None
