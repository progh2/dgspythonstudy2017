class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result

	def sub(self):
		result = self.first - self.second
	
	def div(self):
		result = self.first / self.second
		return result

if __name__ == "__main__":
	a = FourCal()
	b = FourCal()
	a.setdata(4,2)
	b.setdata(3,7)
	print(a.sum())
	print(a.mul())
	print(b.div())
	
