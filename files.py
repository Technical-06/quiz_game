import os
class test:
    def __init__(self):
        self.filename=input("enter file name")
    def test_create(self):
        if not os.path.exists(self.filename):
           open(self.filename,"x").close()# its create file if it doesn't exist and open it in write mode
        else:
            print("file already exists")
    def test_write(self):
        x = input("Enter file content : ")
        f=open(self.filename,"w")# To write in a file
        f.write(x)
        f.close()
    def test_read(self):
        f=open(self.filename,"r")#To read a file
        content=f.read()
        print(content)
        f.close()
    def test_append(self):
        x = input("Enter file content : ")
        f=open(self.filename,"a")#To append a file
        f.write(x)
        f.close()
    def test_delete(self):
        if os.path.isfile(self.filename):
           os.remove(self.filename)# To delete a file
           print("File has been deleted")
        else:
           print("File does not exist")

    def operations(self):
     choice=1
     while choice!=0:
            print("0.Exit")
            print("1.Create")
            print("2.Write")
            print("3.Read")
            print("4.Append")
            print("5.Delete")
            choice=int(input("Enter choice:"))
            if choice==1:
                    print("results:",self.test_create())
            elif choice==2:
                    print("results:",self.test_write())
            elif choice==3:
                    print("results:",self.test_read()) 
            elif choice==4:
                    print("results:",self.test_append())
            elif choice==5:
                    print("results:",self.test_delete())
            elif choice==0:
                    print("exit")
                    exit()
            else:
                    print("No choice is there")
            print()


