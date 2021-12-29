class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelarate(self):
        print("accelerating")
    def change_gear(self):
        print("gear changed")

car= Car("bmw","red","bmw",100)
print(car.start())
print(car.color)