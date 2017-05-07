class Person:
	type = "사람"

	def __init__(self, name="무명씨"):
		self.name = name

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greeting(self):
		print("안녕하세요~ 저는 %s인 %s 입니다!" % (self.type, self.name))

class Student(Person):
	type = "학생"

	def __init__(self, name="무명씨", grade = 1):
		self.name = name
		self.grade = grade
	
	def study(self, n = 1):
		print("나는 %d학년! 공부합니다!" % self.grade)
	
	def play(self, n = 3):
		print("놀자!!")

class Teacher(Person):
	type = "선생님"

	def __init__(self, name="무명씨", major="공통"):
		self.name = name
		self.major = major

	def teach(self):
		print("%s과목 가르치기" % self.major)

	def draft(self, n = 1):
		print("기안하기" * n )

class Hero(Person):
	type = "영웅"
	def __init__(self, name="무명씨", skillname="허찌르기!"):
		self.name = name
		self.skillname = skillname
	
	def skill(self):
		print("필살기, %s!!" % self.skillname)

	

if __name__ == "__main__":
        p1 = Person()
	p1.greeting()
	
	s1 = Student()
	s1.greeting()
	
	s2 = Student("맹구", 3)
	s2.greeting()
	s2.study()
	s2.play()
	s2.study(3)
	s2.study(3)
	
	t = Teacher("함기훈", "프로그래밍")
	t.greeting()
	t.draft()
	t.teach()
	t.draft(100)
	
	h1 = Hero("제로스", "소각")
	h1.greeting()
	h1.skill()
	
	h2 = Hero("사이타마", "잔심펀치!")
	h2.greeting()
	h2.skill()
