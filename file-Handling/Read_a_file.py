import os

# Open the file in read mode
file_path = 'file-Handling/sample.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        content = file.readlines()
        print("Read file Content:")
        line_number = 0
        for line in content:
            line_number += 1
            print(f"Line {line_number}: {line.strip()}")
else:
    print(f"The file '{file_path}' does not exist.")