import fire

class Start_Stage(object):
	def start(self):
		print("Starting Webservers!")

class Stop_Stage(object):
	def stop(self):
		print("Stopping Webservers!")

class Status_Stage(object):
	def status(self):
		print("Status of the Webservers!")

class WebServerManager(object):
	def __init__(self):
		self.start = Start_Stage()
		self.stop = Stop_Stage()
		self.status = Status_Stage()

	def bounce(self):
		self.stop.stop()
		self.start.start()
		self.status.status()

if __name__ == '__main__':
	fire.Fire(WebServerManager)