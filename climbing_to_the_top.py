import fire

class Climber(object):
	def __init__(self, name, stories = 3):
		self.name = name
		self.stories = stories

	def climb(self, stairs_per_stories = 7):
		for story in range(self.stories):
			for stair in range(stairs_per_stories):
				yield stair
			yield "I'm exhausted"
		yield "It's over...."

if __name__ == '__main__':
	fire.Fire(Climber)