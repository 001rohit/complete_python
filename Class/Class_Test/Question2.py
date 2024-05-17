# Print the average of three numbers entered by user by creating a class named 'Average'having a method to calculate and print the average
class Average:
        
    def  set_input(self):
        self.a = int(input("Enter first number: ")) 
        self.b = int(input("Enter second number: ")) 
        self.c = int(input("Enter third number: ")) 
        self.aver = (self.a+self.b+self.c)/3

    def Print_data(self):
        print(f"Average : {self.aver }")

object1 = Average()
object2 = Average()
object1.set_input()
object2.set_input()
object2.Print_data()

