class ServiceConfig():
	def __init__(self, service):
		for key, value in service.items():
			setattr(self, key, value)
