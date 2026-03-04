
try:
    with open('file-Handling/sample.txt', 'r') as file:
        # Read the entire content of the file
        content = file.readlines()
        print("Read file Content:")
        line_number = 0
        for line in content:
            line_number += 1
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"The file 'sample.txt' does not exist.")