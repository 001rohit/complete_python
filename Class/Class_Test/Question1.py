# Write a program to print the area and perimeter of a triangle having sides of 3, 4 and 5units by creating a class named 'Triangle' without any parameter in its constructor.
class Traingle:

    def  __init__(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
        
    def Print_data(self):
        print(f"Area of Traigle is {self.a * self.b * self.c}")
        print(f"Perimeter of Traingle is {self.a + self.b+ self.c }")

object1 = Traingle(3,4,5)
object1.Print_data()

