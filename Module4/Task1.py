

def factorial(n): 
    if n < 2:
        return n
    else:
        return n * factorial(n-1) 


num = int(input("Enter a number:"))

calc = factorial(num)

print(f"factorial of {num} is:{calc}")