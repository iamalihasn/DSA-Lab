number = [x*2 for x in range(1, 11)]

x = iter(number)

for _ in range(len(number)):
    print(next(x))
    
for x in number:
    print(x)