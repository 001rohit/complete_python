# Create a class  circle class with  radius as data member. Create constructors to calculate area and  a method to calculate Circumference.

class circle:
    radius = 0
    pi = 3.14
    circumferance = 2
   
    def __init__(self,radius):
        self.radius=radius
    
    def Print_data(self):
        print("Area of cricle is: ",{self.pi * self.radius *self.radius})
        print("Circumferance of circle is : ",self.circumferance*self.pi*self.radius)

object1 = circle(5)
object1.Print_data()