class grandfather:
    def setdata(self,name,age):
        self.name=name
        self.age=age
    def showdata(self):
        print("name:",self.name)
        print("age:",self.age)
class father(grandfather):
        def getdata(self,status):
            self.status=status
        def showdata(self):
           print("status:",self.status)
class son(father):
    def play(self,game):
       self.game=game

ob=son()
ob.play()
