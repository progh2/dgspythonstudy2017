class TheGirl:
    lastname = "Allina"
    def __init__(self, name):
        self.fullname = name + self.lastname
    
    def fun(self, where):
        print("%s는 술 먹으러 %s에 갔네" % (self.fullname, where))
        
    def love(self, other):
        print("%s, %s 사랑에 빠졌다<3" % (self.fullname, other.fullname))
        
    def __add__(self, other):
        print("아싸! %s, %s 헛 카플 됐다" % (self.fullname, other.fullname))
        
    def __sub__(self, other):
        print("%s, %s 헤어졌다" % (self.fullname, other.fullname))
        
class TheDude:
    lastname = "Kim"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def work(self, where, what):
        print("%s는 %s에서 %s로 일한다" % (self.fullname, where, what))
        
    def meet(self, other):
        print("%s는 %s를 일자리에서 처음에 만났다" % (self.fullname, other.fullname))
        
    def cheat(self, other):
        print("%s, %s 바람을 피웠다ㅠ" % (self.fullname, other.fullname))
        
if __name__ == "__main__":
    girl = TheGirl("Marta")
    boy = TheDude("Dark")
    girl.fun("위스키바")
    boy.work("유명한 위스키바", "바텐더")
    boy.meet(girl)
    girl.love(boy)
    girl + boy
    boy.cheat(girl)
    girl - boy
    
    