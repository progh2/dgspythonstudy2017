class myFortune():
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def __str__(self):
        return self.name

    def myage(self):
        birth = self.birth
        age = 2017 - int(birth[:4]) + 1
        print(age)

    def myzodiac(self):
        birthyear = self.birth[:4]
        animals = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']

        for i in range(len(animals)):
            if int(birthyear) % 12 == i:
                zodiac = animals[i]

        print(zodiac+'띠')

    def myconstellation(self):
        birthday = self.birth[4:]
        x = int(birthday)

        if 120 <= x <= 218:
            print('물병자리')
        elif 219 <= x <= 320:
            print('물고기자리')
        elif 321 <= x <= 420:
            print('양자리')
        elif 421 <= x <= 520:
            print('황소자리')
        elif 521 <= x <= 621:
            print('쌍둥이자리')
        elif 622 <= x <= 722:
            print('게자리')
        elif 723 <= x <= 822:
            print('사자자리')
        elif 823 <= x <= 922:
            print('처녀자리')
        elif 923 <= x <= 1021:
            print('천칭자리')
        elif 1022 <= x <= 1121:
            print('전갈자리')
        elif 1122 <= x <= 1221:
            print('사수자리')
        else:
            print('염소자리')

jy = myFortune('기훈', '19820108')

jy.myage()
jy.myzodiac()
jy.myconstellation()