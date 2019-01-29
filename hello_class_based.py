import fire

class Welcome(object):
	def hello(self, name):
		return f"Welcome to my course: {name}"

	def multiply(self, x, y):
		return f" x * y = {x * y}"

if __name__ == '__main__':
	fire.Fire(Welcome)