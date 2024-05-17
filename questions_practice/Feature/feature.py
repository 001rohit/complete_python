import unittest
# from .functionality import

def reverse_string(value):
    return value[::-1]

# res = reverse_string("Hellow")
# print(res)

# class Employee:
#     def __init__(self ,id,name,address):
#         self .id = id
#         self .name = name
#         self .address = address
        

#     def display_data(self):
#         print(f"id:{self.id})\n",
#                 f"name: {self.name}\n",
#                 f"address: {self.address}")
        
   
class FeatureUnitTesting(unittest.TestCase):

    def setup(self):
        self.value = "Hellow"
        self.output = "wolleH"
        

    def test_reverse_string(self):
         res = reverse_string("Hellow")
         self.assertEqual(res,"wolleH")
      
#    def test2_findEven(self):
#          res = check_num(self.value1)
#          self.assertEqual(res,)
    def test_display_employee_data(self):
        name= self.emp
    def tearDown(self):
        self.value = None
        self.output = None

    
if __name__ == '__main__':
          unittest.main()