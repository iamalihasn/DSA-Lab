import os 

user_input = ""

# Check if the file exists, if not create and write to it, else append to it

if not os.path.exists("file-Handling/output.txt"):
    with open("file-Handling/output.txt","wt") as file:
        user_input = input("Enter text to write the file : ")
        file.write(user_input)
    
    print("Data write successfully in output.txt")
else:
   
    while True:
        user_input = input("Enter additional text to add : ")
        
        # Check if the user wants to stop appending data

        if user_input == "25":
            print("=======================================")
            break
        with open("file-Handling/output.txt","at") as file:
            file.write(f"\n{user_input}")

        print("Data append successfully in output.txt")
        print("=======================================")
    
    print("Final content of output.txt")
    with open("file-Handling/output.txt","rt") as file:
        data = file.read()
    
    print(data)