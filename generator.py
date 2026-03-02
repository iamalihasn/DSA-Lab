def my_generator():
    yield 1
    yield 2
    yield 3

x = my_generator()
print(next(x))  # Output: 1
print(next(x))  # Output: 2
print(next(x))  # Output: 3
# print(next(x))  # This will raise StopIteration since there are no more items to yield.

def generators():
    for i in range(1,21):
        yield i

for number in generators():
    print(number)  # Output: 1, 2, 3, ..., 20

def squares(n):
    for i in range(1,n+1):
        yield i**2


# for square in squares(5):
#     print(square)  # Output: 1, 4, 9, 16, 25

squares = (x**2 for x in range(1, 10))
print(next(squares))