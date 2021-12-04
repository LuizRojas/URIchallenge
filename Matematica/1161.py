def factorial(n):
    produto = 1
    for i in range(1, n+1):
        produto *= i
    return produto
    
entrada = input().split()
print(factorial(int(entrada[0])) + factorial(int(entrada[1])))
