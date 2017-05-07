# Person 클래스와 이 클래스를 상속받은 Student, Teacher, Hero 클래 예제입니다.

# 사람 클래스. 다른 클래스의 부모 클래스가 됩니다.
class Person:
	type = "사람"		# 클래스 변수. Person의 객체들은 모두 이 값을 가지며 공유합니다. 

	# 생성자. 인자로 이름을 받으며 생략할 때 무명씨라는 이름을 기본값으로 가집니다.
	def __init__(self, name="무명씨"):
		self.name = name	# 생성자 파라메터로 받아온 name 을 멤버변수 name을 만들어 저장합니다.

	# 멤버변수 name을 변경하는 메소드
	def setName(self, name):
		self.name = name

	# 멤버변수 name을 가져오는 메소드
	def getName(self):
		return self.name

	# 멤버변수 name과 클래스변수 type을 활용해서 인사하는 메소드
	def greeting(self):
		# 클래스 변수는 바로 변수명을 사용해서 사용할 수 있습니다. 
		print("안녕하세요~ 저는 %s인 %s 입니다!" % (type, self.name))
		# 아래 2개도 똑같이 동작합니다. 
		# 클래스 변수 type을 강조
		# print("안녕하세요~ 저는 %s인 %s 입니다!" % (Person.type, self.name))
		# 클래스 변수는 멤버 변수로도 참조가 가능합니다. 
		# print("안녕하세요~ 저는 %s인 %s 입니다!" % (self.type, self.name))

# Person클래스를 상속받은 학생 클래스
class Student(Person):
	type = "학생"		#클래스 변수를 학생으로 덮어씁니다.

	# 학생 클래스의 생성자는 학년도 추가로 지정 가능합니다. 생략하면 1학년
	# 주의할 점이 기본값을 가지는 파라메터는 뒤쪽에 와야합니다.
	def __init__(self, name="무명씨", grade = 1):
		self.name = name	# 멤버변수 name 생성 후 지정
		self.grade = grade	# 멤버변수 grade 생성 후 지정
	
	# 공부하는 메소드. 인자값을 줘서 반복시킬 수 있습니다.
	def study(self, n = 1):
		print("나는 %d학년! 공부합니다!" % self.grade)
	
	# 노는 메소드. 인자값을 줘서 반복시킬 수 있습니다. 
	def play(self, n = 3):
		print("놀자!!")

# 선생님 클래스
class Teacher(Person):
	type = "선생님"

	# 두번째 인자로 과목을 지정합니다.
	def __init__(self, name="무명씨", major="공통"):
		self.name = name
		self.major = major

	def teach(self):
		print("%s과목 가르치기" % self.major)

	# ㅠㅠ 기안기안
	def draft(self, n = 1):
		print("기안하기" * n )

# 원펀맨 스타일 영웅 클래스 
class Hero(Person):
	type = "영웅"
	def __init__(self, name="무명씨", skillname="허찌르기!"):
		self.name = name
		self.skillname = skillname
	
	def skill(self):
		print("필살기, %s!!" % self.skillname)

	
# 모듈 관련 내용 참고. 이 클래스를 다른 클래스에서 가져와 실행할 때 이 코드들은 실행되지 않습니다.
# 이 클래스를 바로 실행할 때만 실행되게 하는 코드
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
