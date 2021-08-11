def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.item():
    # print(key)
    # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(add(1, 4, 6, 7))
print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw["colour"]
        self.seats = kw["seats"]
        self.year = kw["year"]


my_car = Car(make="VW", model="Golf")
print(my_car.make, my_car.model)