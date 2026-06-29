"""def analyze_string (s):
    name=input("enter a string :")
    length=len(s)
    print("length:",length)

 analyze_string(s)"""
class  car:
    def __init__(self , brand,model,):
        self.brand=brand
        self.model=model

    def  display_info(self):
        print("car brand:",self.brand)
        print("car model:",self.model)

car_demo1=car("mahindra", "mahindra thar")
car_demo2=car("maruti suzuki","nexa")
car_demo1.display_info()
car_demo2.display_info()


   