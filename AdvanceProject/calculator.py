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
            #switch case
            match choice: 
                case 0:
                        print("existing")
                        exit()
                case 1:
                        print("results:",self.add())
                case 2:
                        print("results:",self.mul())
                case 3:
                        print("results:",round(self.div(),2)) #for rounding upto two decimal places
                case 4:
                        print("results:",self.sub())  
                case default:
                        print("No choice is there")
       