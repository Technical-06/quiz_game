from logging import PercentStyle
class student:
    def __init__(self,name,roll,percent):
        self.name=input("enter name")
        self.roll=int(input("enter roll"))
        self.percent=float(input("enter Percent"))
    def display(self):
        print("Name",self.name)
        print("Roll",self.roll)
        print("Percent",self.percent)
class employee(student):
    def showdata(self):
        print("i am an employee")

a=employee("sonal",82,100)
a.showdata()
a.display()

