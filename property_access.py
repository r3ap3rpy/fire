import fire

class Calculator(object):
	def __init__(self, number):
		self.number = number
		self.double = number * 2
		self.triple = number * 3
		self.quadruple = number * 4

if __name__ == '__main__':
	fire.Fire(Calculator)