'''
down below you can see that
child class introduces new instance
=> it's bad as you need to put additional
info when creating that child class which
breaches Barbara Liskov principle
'''
class Slug:
	def __init__(self):
		self.name = name

	def crawl(self):
		orint('slime trail!')


class Snail(Slug):
	def __init__(self, name, shell_size):
		super().__init__(name)
		self.name = name
		self.shell_size = shell_size


def race(gastropod_one, gastropod_two):
	gastropod_one.crawl()
	gastropod_two.crawl()


race(Slug('Naruto'), Slug('Sasuke'))
# ones below will raise error as we
# don't specify `shell_size`
race(Snail('Lee'), Snail('Kiba'))


'''
one below is erroneous as child class
must use all of the behaviour of the superclass
'''
class Bird:
	def fly(self):
		print('flying')


class Hummingbird(Bird):
	def fly(self):
		print('zzzooomm!')


# Penguin cannot fly, how to deal with it?
# Composition here is a better option
class Penguin(bird):
	def fly(self):
		# ???
		pass


'''
we can resuse superclass() methods to specialize
CHILD'S behaviour that is based on the parent's
original behaviour.
But in this case substitutability becomes extremely
important
'''
class Teller:
	def deposit(self, amount, account):
		account.deposit(amount)


class CorruptTeller(Teller):
	def __init__(self):
		self.coffers = 0

	def deposit(self, amount, account):
		self.coffers += amount * 0.01
		super().deposit(amount * 0.99, account)


'''
multiple inheritance

mro:
1. Liger -> Lion -> BigCat -> object -> Tiger -> BigCat -> object
2. remove duplicates
3. Construct result: Liger -> Lion -> Tiger -> BigCat -> object
'''
class BigCat:
	def eat(self):
		return ['rodents']


class Lion(BigCat):
	def eat(self):
		return ['wildebeest']


class Tiger(BigCat):
	def eat(self):
		return ['water buffalo']


class Liger(Lion, Tiger):
	def eat(self):
		return super().eat() + ['rabbit', 'cow', 'pig', 'chicken']


'''
+ there is 'cooperative multiple inheritance'. In this case every class
must have stellar substitutability. Python will go above parents even
after it finds desired method: super().some_method()
'''
class BigCat:
	def eat(self):
		return ['rodents']


class Lion(BigCat):
	def eat(self):
		return super().eat() + ['wildebeest']


class Tiger(BigCat):
	def eat(self):
		return super().eat() + ['water buffalo']


class Liger(Lion, Tiger):
	def eat(self):
		return super().eat() + ['rabbit', 'cow', 'pig', 'chicken']


'''
Python has option to resemble interfaces
with Abstractmethod.
Defining additional methods on a subclass of
an abstract base class works just fine, but
methods defined in Abstractclass must be realized
'''
from abc import ABC, abstractmethod


class Predator(ABS):
	@abstractmethod
	def eat(self, prey):
		pass


class Owl(Predator):
	def eat(self, prey):
		print(f"Hover over {prey}")


class Bear(Predator):
	def eat(self, prey):
		print(f"Mauling {prey}")

	def roar(self):
		print(f"Bear is roaring!")


class Chameleon(Predator):
	def eat(self, prey):
		print(f'Shooting tonguw at {prey}')


if __name__ == '__main__':
	bear = Bear()
	bear.eat('deer')
	owl = Owl()
	owl.eat('mouse')
	chameleon = Chameleon()
	chameleon.eat('fly')


'''
Also we can use Mixin to resemble interface
'''
class SpeakMixin:
	def speak(self):
		name = self.__class__.__name__.lower()
		print(f'The {name} says hello!')

class RollOverMixin:
	def roll_over(self):
		pritn('Did a barrel roll!')


class Dog(SpeakMixin, RollOverMixin):
	pass


dog = Dog()
dog.speak()
dog.roll_over()
