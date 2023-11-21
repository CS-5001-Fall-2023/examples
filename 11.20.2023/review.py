class Review:

	def __init__(self, asin, rid, overall):
		self.asin = asin
		self.rid = rid
		self.overall = overall

	def __str__(self):
		return f'{self.asin} - {self.rid} - {self.overall}'

	def __repr__(self):
		return self.__str__()