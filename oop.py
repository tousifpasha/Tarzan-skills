# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def features(self, color):
#         return "{} is {} and its price is {}".format(self.name, color, self.price)
# obj_1= Car('BMW','30lakh')
# print(obj_1.features('red'))



class Circle:
    pi = 3.14
    y=0
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    def setradius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius*new_radius*self.pi

    def getarea(self, new_rad_value):
        return new_rad_value*new_rad_value*self.pi

    def circumference(self, new_radius):
        return new_radius*self.pi*2
c = Circle()
y= int(input("Enter the radius to find a area of a circle : "))
c.setradius(y)
x = c.getarea(7)
z = c.circumference(y)
print('Radius is : ', c.radius)
print('Area is : ', c.area)
print('Circumference of a circle : ', z)
print('New Area is : ', x)



