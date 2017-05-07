class snack:
    price = 0
    name = "과자"

    def __init__(self, price, name):
        self.price = price
        self.name = name

    def print_name_price(self):
        print(self.name + "과자의 가격은 " + str(self.price) + " 원 입니다.")

    def up_price(self, up_price):
        self.price = self.price + up_price
        print(self.name + "과자의 가격이 " + str(up_price) + " 원 인상되었습니다.")

s1 = snack(900, "새우깡")
s2 = snack(1200, "포카칩")
s3 = snack(600, "뿌셔뿌셔")

s1.print_name_price()
s2.print_name_price()
s3.print_name_price()

s2.up_price(100)

s2.print_name_price()
