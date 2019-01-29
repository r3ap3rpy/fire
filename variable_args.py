import fire 

def kindof(*args):
	for arg in args:
		print(f"Got argument: {arg}")

if __name__ == '__main__':
	fire.Fire(kindof)