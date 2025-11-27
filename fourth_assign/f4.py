class Vehicle:
    brand='bmw'
    model="beamer"


class bike(Vehicle):
    engine_cc=350
class car(Vehicle):
    seat=7


v=Vehicle()
b=bike()
print(b.engine_cc, b.brand,b.model)


c=car()
print(c.seat, c.brand,c.model)
