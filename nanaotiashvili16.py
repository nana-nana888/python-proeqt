def decorator (func):
    def wrapper(number):
        if number < 0:
            raise ValueError("number must be positive")
        result = func(number)
        print(f"result: {result}")
        return result
    return wrapper

@decorator
def return_number(number):
    return number

print(return_number(3))
print(return_number(-3))







class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        if number < 0:
            raise ValueError("number must be positive.")
        result = self.func(number)
        print(f"result: {result}")
        return result

def return_number(number):
    return number

functor = Functor(return_number)

print(functor(5))







import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs) 
        end_time = time.time() 
        elapsed_time = end_time - start_time  
        print(f"{func.__name__} Function completed  {elapsed_time:.6f} second")
        return result
    return wrapper

@timing_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = example_function(100)  
print(f"result: {result}")

