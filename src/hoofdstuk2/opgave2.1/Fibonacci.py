def fibonacci(n, diepte=0):
    if n <= 2:
        return 1
    diepte += 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
