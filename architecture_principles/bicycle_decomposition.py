'''
First one is worse than the second one as it lacks
inversion of control. I.e. `Bicycle` hinges on the
`Tire() & Frame()` => upgrading is difficult
'''
class Tire:
	def __repr__(self):
		return 'A rubber Tire'


class Frame:
	def __repr__(self):
		return 'An aluminum frame'


class Bicycle:
	def __init__(self):
		self.front_tire = Tire()
		self.back_tire = Tire()
		self.frame = Frame()

	def print_specs(self):
		print(f"Frame: {self.frame}")
		print(f"Front tire: {self.front_tire}, Back tire: {self.back_tire}")


if __name__ == '__main__':
	bike = Bicycle()
	bike.print_specs()


'''
Inversion of control says that instead of creating instances
of dependencies in your class, you can pass in existing instances
for the class to make use of. The control of dependency creation
is inverted by giving the control to whatever code is creating
a Bicycle.
'''
class Tire:
	def __repr__(self):
		return 'A rubber Tire'


class Frame:
	def __repr__(self):
		return 'An aluminum frame'


class CarbonFiberFrame:
	def __repr__(self):
		return 'A carbon fiber frame'


class Bicycle:
	def __init__(self, front_tire, back_tire, frame):
		self.front_tire = front_tire
		self.back_tire = back_tire
		self.frame = frame

	def print_specs(self):
		print(f"Frame: {self.frame}")
		print(f"Front tire: {self.front_tire}, Back tire: {self.back_tire}")


if __name__ == '__main__':
	bike = Bicycle(Tire(), Tire(), Frame())
	bike.print_specs()
	new_bike = Bicycle(Tire(), Tire(), CarbonFiberFrame())
	new_bike.print_specs()
