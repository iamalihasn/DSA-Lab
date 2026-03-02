import os
from pathlib import Path
# read file
"""
file = open("myfile.txt","r")
print(file.read())
file.close()

# write file
file = open("myfile.txt","w")
file.write("Hello World !")
"""

# with statement
with open("myfile.txt","r") as file:
    print(file.read())

# with open("myfile.txt","w") as file:
#     file.write("Hello Reyan")

# with open("myfile.txt","a") as file:
#     file.write("\nFather : Ravi Kumar")
#     file.write("\nMother : Rusksana")
#     file.write("\nSister : Riya")

# with open("myfile.txt","a") as file:
#     content = file.read()
#     print(content)


# check if file exists

if os.path.exists("myfile.txt"):
    with open("myfile.txt","r") as file:
        print(file.read())
else:
    print("File does not exist")

# also we can use try except block to handle file not found error
try:
    with open("myfiles.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

#also we can use os.path.isfile() to check if the path is a file or not

file_path = Path("myfile.txt")
if file_path.exists ():
    with open(file_path,"r") as file:
        print(file.read())
else:
    print("File does not exist")