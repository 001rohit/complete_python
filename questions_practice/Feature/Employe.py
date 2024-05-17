class Employee:
    def __init__(self ,id,name,address):
        self .id = id
        self .name = name
        self .address = address
        

    def display_data(self):
        print(f"id:{self.id})\n",
                f"name: {self.name}\n",
                f"address: {self.address}")
        
        
obj1 = Employee(12,'rohit','kolar road bhopal')
obj1.display_data()