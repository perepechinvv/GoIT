n = int(input('Input n = '))

def fibonacci(n):
    if n == 0:
        return 0    
    elif n < 2:
        return 1
    else:   
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(n)
print(f'Fibonachi {result}')  
