class Serving_bot:
    def init(self):
        self.menu = ["물", "의자", "테이블"]
        self.price = [0, 100, 500]

        self.list = ""
        self.total = 0

    def hi(self):
        print("안녕")
    
    def introduce(self):
        print("매장 소개 : ㅇㅇㅇㅇㅇ")

    def request_water(self):
        print("물은 셀프")

    def show_menu(self):
        print("메뉴판:\n 1 : 의자 : 100만원\n 2 : 테이블 : 500만원 ")

    def add_order(self, num):
        self.total = self.total + self.price[num]
        self.list = self.list + self.menu[num] + "\n"
        print(self.menu[num] + "추가")

    def check_order(self):
        print(self.list)

    def calc_order(self):
        print(str(self.total) + "만원")

    def go_home(self):
        print("bye!")


if __name__ == "__main__":

    bot = Serving_bot()
    bot.init()

    while True:

        bot.hi()

        print(
            "1.매장소개\n"
            "2.물주세요\n"
            "3.메뉴보기\n"
            "4.주문하기\n"
            "5.이전 계산서 확인\n"
            "6.집갈래요\n"
            )

        ordering_num = int(input("번호로 입력 : "))

        if ordering_num == 1:
            bot.introduce()

        elif ordering_num == 2:
            bot.request_water()

        elif ordering_num == 3:
            bot.show_menu()

        elif ordering_num == 4:
            stop = 1
            while stop == 1:
                order_menu_num = int(input("주문할 번호 입력 :"))
                bot.add_order(order_menu_num)
                stop = int(input("계속 주문을 원하면 1을 눌러주세요."))
            bot.check_order()
            print("주문 완료")

        elif ordering_num == 5:
            bot.check_order()
            bot.calc_order()

        elif ordering_num == 6:
            bot.go_home()
            break
        else:
            print("잘못누름 ㅇㅇ 다시 눌러")

