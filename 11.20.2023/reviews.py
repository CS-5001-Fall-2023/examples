from review import Review

class Reviews:

	def __init__(self):
		# key is reviewerId
		self.byrid = {}
		# key is asin
		self.byasin = {}		
		# top rated	
		# list sorted by overall score
		self.top_rated = []	
		self.recently_sorted = False

	def get_top_rated(self, cutoff):
		""" Returns list of top rated
		reviews. The cutoff specifies the 
		number of reviews to return.
		"""
		if not self.recently_sorted:
			self.top_rated.sort(reverse=True, key=self.sort_by_overall)
			self.recently_sorted = True
		return self.top_rated[:cutoff]

	def add_review(self, review):
		if review.rid in self.byrid:
			self.byrid[review.rid].append(review)
		else:
			reviews = []
			reviews.append(review)
			self.byrid[review.rid] = reviews

		if review.asin in self.byasin:
			self.byasin[review.asin].append(review)
		else:
			reviews = []
			reviews.append(review)
			self.byasin[review.asin] = reviews

		# this will maintain the list in sorted order
		# always
		# consider whether it is better to have it always
		# sorted versus sorting only when
		# get_top_rated gets called
		self.top_rated.append(review)
		self.recently_sorted = False
		# self.top_rated.sort(reverse=True, key=self.sort_by_overall)
		# self.top_rated.sort(reverse=True, key=lambda review: review.overall)

		# sorted(self.top_rated, ...)

	def sort_by_overall(self, review):
		return review.overall

	def get_by_asin(self, asin):
		if asin not in self.byasin:
			return None
		return self.byasin[asin]

