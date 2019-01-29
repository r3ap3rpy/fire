import fire

def hello(name):
	return f"Welcome to my course: {name}"

def divide(x, y):
	return f" x / y = {x / y}"


if __name__ == '__main__':
	fire.Fire({
		'welcome' : hello,
		'math' : divide
		})