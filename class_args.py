import fire

class Calculator(object):
	def __init__(self):
		pass

	def add(self, x, y):
		return x + y

	def multiply(self, x, y):
		return x * y

	def divide(self, x, y):
		return x / y

if __name__ == '__main__':
	fire.Fire(Calculator)