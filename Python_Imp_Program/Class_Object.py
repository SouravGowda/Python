class car():
    def __init__ (self,model,year,price):
        self.model = model
        self.year = year
        self.price = price

    def price_increment(self):
        self.price = int(self.price*1.15)

class supercar(car): #INHERITANCE
    def __init__(self,model,year,price,cc):
        super.__init__(model,year,price )
        self.cc=int(cc)

honda=supercar('city',2017,1500000,1500)
tata=car('harrier',2017,1700000)

honda.cc=1500

print(honda.price)
honda.price_increment()
print(honda.price)