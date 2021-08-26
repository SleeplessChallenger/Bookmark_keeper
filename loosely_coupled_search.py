import re


class CleanQuote:
	def __init__(self, quote):
		print('__init__')
		self.quote = quote

	def _remove_spaces(self, quote):
		quote = quote.strip()
		resulted_quote = re.sub(r'\s+', '', quote)
		return resulted_quote

	def _normalize(self, quote):
		resulted_quote = quote.casefold()
		return resulted_quote

	def _remove_quotes(self, data):
		query = re.sub(r' "" ', '', data)
		return query

	@property
	def quote(self):
		print('getter')
		return self._quote
	
	@quote.setter
	def quote(self, data):
		print('setter')
		no_spaces_quote = self._remove_spaces(data)
		no_quotes = self._remove_quotes(no_spaces_quote)
		normalized_quote = self._normalize(no_quotes)
		self._quote = normalized_quote


if __name__ == '__main__':
	search_query = input('Enter your quote here: ')
	result = CleanQuote(search_query)
	print(result.quote)
