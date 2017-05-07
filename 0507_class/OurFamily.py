class OurFamily:
    lastname = "Allina"
    
    def __init__(self, name):
        self.fullname = name
    def travel(self,where):
        print("%s, %s  여행을 간다" % (self.fullname, where))

me = OurFamily("Marta")
me.travel("을릉도")