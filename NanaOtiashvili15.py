class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "გასაყიდი"

    def sell(self, buyer, loan_amount=None):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული"
            print(f"ბინა გაიყიდა {buyer.name}-ზე. სტატუსი: {self.status}")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული სესხით"
            buyer.loan += loan_amount
            print(f"ბინა გაიყიდა {buyer.name}-ზე. სტატუსი: {self.status}")



owner = Person(name="ანა")
buyer = Person(name="საბა")


house = House(ID="112233", price=50000, owner=owner)

house.sell(buyer)

house.sell(buyer, loan_amount=51000)

print(owner)
print(buyer)
