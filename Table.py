def table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

if __name__ == "__main__":
    number = int(input("Enter number : "))
    table(number)