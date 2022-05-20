#Calculator
class calc():
#parameterized constructor
    def __init__(self):
        self.x=int(input("Enter first number"))
        self.y=int(input("Enter second number"))
    def add(self):
        return self.x+self.y 
    def mul(self):
        return self.x*self.y 
    def div(self):
        return self.x/self.y 
    def sub(self):
        return self.x-self.y  
class perform_operations(calc):
    def operations(self):
        choice=1
#Looping until choice gets 0
        while choice!=0:
            print("0.Exit")
            print("1.Add")
            print("2.Mul")
            print("3.Div")
            print("4.Sub")
            choice=int(input("Enter choice:"))
            if choice==1:
                    print("results:",self.add())
            elif choice==2:
                    print("results:",self.mul())
            elif choice==3:
                    print("results:",round(self.div(),2)) #for rounding upto two decimal places
            elif choice==4:
                    print("results:",self.sub())
            elif choice==0:
                    print("existing")
            else:
                    print("No choice is there")
            print()
#Creating object of child class
ob=perform_operations()
ob.operations()
    