class BankCard:
    def __init__(self, number, expiry_year, balance):
        self.number = number
        self.expiry_year = expiry_year
        self.balance = balance

    def pay(self, amount, current_year):
        if current_year > self.expiry_year:
            print("Karta muddati tugagan")
        elif amount > self.balance:
            print("Balans yetarli emas")
        else:
            self.balance -= amount
            print("To‘lov amalga oshdi")

card = BankCard("8600 **** **** 1234", 2027, 2000)
card.pay(600, 2026)
print("Balans:", card.balance)
