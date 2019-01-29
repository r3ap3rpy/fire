import fire

def hello(name):
	return f"Welcome to my course: {name}"

if __name__ == '__main__':
	fire.Fire(hello)