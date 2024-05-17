import unittest

def  Check_res(value):
     return value[::-1]
# res = Check_res("Rohit")
# print(res)
class FeatureUnitTesting(unittest.TestCase):

    def setup(self):
        self.value = "Rohit"
        self.output = "tihoR"

    def Check_value(self):
        res = Check_res("Rohit")
        self.assertEqual(res,"tihoR")

    def tearDown(self):
        self.value = None
        self.output = None

    
    if __name__ == '__main__':
          unittest.main()    