import fire 

#def kindof(**kwargs):
#	for key, value in kwargs.items():
#		print(f"Got key: {key} with value: {value}")

def kindof(**kwargs):
	for key in kwargs:
		print("Got key: {} with value: {}".format(key,kwargs[key]))

if __name__ == '__main__':
	fire.Fire(kindof)