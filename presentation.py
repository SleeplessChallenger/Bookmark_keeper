import commands
from collections import OrderedDict
import os


class Option:
	def __init__(self, name, command, prep_step=None, msg='{message}'):
		self.name = name
		self.command = command
		self.prep_step = prep_step
		self.msg = msg


	def __str__(self):
		return f"Command: {self.name}"

	def _prune_string(self, string):
		return '\t'.join(str(col) if col else 'None'
			for col in string)

	def choose(self):
		data = self.prep_step() if self.prep_step else None
		# after adding ABC in `commands` and refactoring
		# `execute()` we don't need check if data is present
		status, phrase = self.command.execute(data)
		# phrase takes those return strings

		outcome = ''
		if isinstance(phrase, list):
			for p in phrase:
				# as p == (_, _, _), we need
				# to change format
				pruned_string = self._prune_string(p)
				outcome += '\n' + pruned_string
		else:
			outcome = phrase

		if status is True and outcome is not None:
			print(outcome)
			# print(self.msg.format(message=outcome))
		else:
			print(self.msg)


def print_options(options):
	for option, obj in options.items():
		print(f"{option} & {obj}")


def isValid(choice, options):
	return choice.upper() in options 


def prompt_input(options):
	choice = input('Put your variant (in either case): ').strip()
	while not isValid(choice, options):
		print('Invalid option, choose from presented below')
		print_options(options)
		choice = input('Put your variant: ').strip()

	return options[choice.upper()]


def get_user_choice(column, required=True):
	user_input = input(f'Put {column}: ').strip() or None
	while not user_input and required:
		user_input = input(f'Put {column}').strip() or None

	return user_input


def add_bookmark():
	return {
		'title': get_user_choice('title'),
		'URL': get_user_choice('url'),
		'notes': get_user_choice('notes', required=False)
	}


def delete_bookmark():
	return {
		'id': get_user_choice('id')
	}


def get_github():
	return {
		'username': get_user_choice('GitHub username'),
		'timestamp': get_user_choice('Preserve timestamps',
			required=False)
				in {'Y', 'y', None}
		# if nothing is provided -> still True
	}


def update_bookmark():
	col = get_user_choice('Enter col to edit')

	return {
		'id': get_user_choice('id'),
		'new info': {col: get_user_choice(f'Enter new data for {col}')}
	}


def clear_screen():
	name = 'cls' if os.name == 'nt' else 'clear'
	os.system(name)


def application_loop():
	clear_screen()

	options = OrderedDict({
		'A': Option('Add a Bookmark',
					commands.AddBookmark(),
					prep_step=add_bookmark,
					msg='Bookmark was added!'),

		'B': Option('List bookmarks by date',
					commands.ListBookmarks(),
					msg='Listed by date'),

		'T': Option('List bookmarks by title',
					commands.ListBookmarks(order_by='title'),
					msg='Listed by title'),

		'D': Option('Delete a bookmark',
					commands.DeleteBookmark(),
					prep_step=delete_bookmark,
					msg='Bookmark was deleted'),

		'G': Option('Add starred from GitHub',
					commands.AddGitHub(),
					prep_step=get_github,
					msg='Added from GitHub'),

		'U': Option('Update bookmark',
					commands.UpdateBookmark(),
					prep_step=update_bookmark,
					msg='Bookmark was updated'),

		'Q': Option('Quit', commands.QuitProgram()),
	})

	print_options(options)

	user_choice = prompt_input(options)
	# get back `Option` class which has particular
	# command hooked up already
	clear_screen()
	user_choice.choose()

	# to enable user to observe the
	# return message
	_ = input("Just pres to proceed")


if __name__ == '__main__':

	while True:
		application_loop()
