class mobile:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def features(self,color):
        return "The best mobile is {} and its price is {} \ncolor : {} ".format(self.name, self.price, color)
    def specification(self,Display,Processor,Front_camera,Rear_camera,OS,RAM,Storage,Battery_capacity):
        return "Specification\n\tDispay : {}\n\tProcessor : {} \n\tFront Camera : {}\n\tRear camera : {}\n\tOS : {}\n\tRAM : {}\n\tStorage : {}\n\tBattery capacity: {}".format(Display,Processor,Front_camera,Rear_camera,OS,RAM,Storage,Battery_capacity)
    def behavior(self,behavior):
        return "it's  {}".format(behavior)
mobilephone=mobile('Vivo v17 pro','24000')
print(mobilephone.features('Blue/Gold'))
print(mobilephone.specification('6.44inch','Qualcomm Snapdragon','32MP + 8MP','48MP','Andriod 9.1','8GB','128GB','4100 mAh',))
print(mobilephone.behavior('Battery backup is good and it has good camera quality'))
