
class products:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        products.count+=1
    @classmethod
    def get_count(cls):
        print(f"total products created are {cls.count}")

    @staticmethod
    def dis_price(price, disc):
        final_price=price-(disc*price/100)
        print(final_price)
    

p1=products("book",300)
p2=products("pen",31)

products.dis_price(p1.price,10)
products.get_count()

