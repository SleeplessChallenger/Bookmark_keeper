# function level

from random import choice
import json


FOODS = [
	'pizza',
	'burgers',
	'salad',
	'soup',
]


def get_json(food):
	return json.dumps({'food': food})


def get_xml(food):
	return f'<response><food>{food}</food></response>'


def format_function(accept=None):
	formats = {
		'application/json': get_json,
		'application/xml': get_xml
	}

	return formats.get(accept, lambda val: val) 


def random_food(request):
	food = choice(FOODS)

	format_function = format_function(request.headers.get('Accept'))

	return format_function(food)


# class level

'''
one below is bad as it sets attributes
outside of __init__
'''
class Book:
	def __init__(self, data):
		self.title = data['title']
		self.subtitle = data['subtitle']
		self.set_display()


	def set_display(self):
		if self.title and self.subtitle:
			self.display_title = f'{self.title}: {self.subtitle}'
		elif self.title:
			self.display_title = self.title
		else:
			self.display_title = 'Untitled'

'''
the one below is much better
as it uses @property
'''

class Book:
	def __init__(self, data):
		self.title = data['title']
		self.subtitle = data['subtitle']

	@property
	def display_title(self):
		if self.title and self.subtitle:
			return f"{self.title}: {self.subtitle}"
		elif self.title:
			return f"{self.title}"
		else:
			return 'Untitled'


'''
soon Author may become a separate concern
and it'll be better to encapsulate it in a
separate class.
But to enable backward compatibily we need
to enable user still use features through Book
for some time
'''
import warnings


class Book:
	def __init__(self, data):
		# keeps data while user still needs it
		self.author_data = data['author_data']
		self.titke = data['title']
		self.subtitle = data['subtitle']
		self.author_class = Author(self.author_data)


	@property
	def author_for_display(self):
		warnings.warn('Do not use this anymore!', DeprecationWarning)
		return self.author_class.author_for_display

	@property
	def author_for_citation(self):
		warnings.warn('Do not use this anymore!', DeprecationWarning)
		return self.author_class.author_for_citation


class Author:
	def __init__(self, author_data):
		self.first_name = author_data['first_name']
		self.second_name = author_data['second_name']


	@property
	def author_for_display(self):
		return f"{self.first_name} {self.second_name}"

	@property
	def author_for_citation(self):
		return f"{self.second_name} {self.first_name[0]}"
