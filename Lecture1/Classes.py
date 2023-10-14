class Car:
    name:str = "ford"
    model:str
    color:str
    price:int = 2000
    def discount(self, per):
        print(self.name)
        self.price -= self.price * per
    def __init__(self, name="", price=10000):
        self.name = name
        self.price = price

car1 = Car()
car1.name = "Toyota"
car1.model = 2001
car1.color = "blue"
car1.discount(0.5)
print(f'{car1.name} price model: {car1.model} after discount {car1.price}')

car2 = Car("Tesla", 30000)
print(car2.name + ' ' + str(car2.price))