class Student:

	def __init__(self, name, grades, id):
		self.name = name
		self.grades = grades
		self.id = id


	def __str__(self):
		return f'{self.name} - {self.id} - {self.grades}'