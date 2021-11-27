def factorial(n):
    produto = 1
    for i in range(1, n+1):
        produto *= i
    return produto
    
e1 = int(input())
e2 = int(input())

print(factorial(e1) + factorial(e2))
