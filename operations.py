import os
# #read a file
f=open("Files/file1.txt","r")
content=f.read()
for x in f:
    print(content)
f.close()

 #write in a file
f=open("sonal.txt","w")
f.write("\n")
f.write("hello guys!\nguys")
f.close()

#delete a file
file = "Files/file1.txt"
if os.path.isfile(file):
  os.remove(file)
  print("File has been deleted")
else:
  print("File does not exist")

# #append in a file
f=open("sonal.txt","a")
f.write("how's you")
f.close()

#its check if file already exist is will show error otherwise it will create it
f=open("sonal.txt","x")
f.write("my name is sonal.i belong to knl")
f.close()



