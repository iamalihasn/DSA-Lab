

def my_decorator(func):
    def wrapper(a,b):
        print("Before the function call")
        result = func(a, b)
        print("After the function call")
        return result
    
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))  # Output: Before the function call, After the function call, 8