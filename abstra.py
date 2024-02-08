from abc import ABC,abstractmethod
class Mobile(ABC):
    @abstractmethod
    def internet(self):
        pass
    

class Iphone(Mobile):
    def internet(self):
        print("It has 5g internet")
        

class Oppo(Mobile):
    def internet(self):
        print("It has 4G internet")

m=Mobile()
m.internet()
ip=Iphone()
ip.internet()
op=Oppo()
op.internet()
