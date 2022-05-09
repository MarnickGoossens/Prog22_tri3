global diepte
diepte = 0


def fibonacci(n):
    if n <= 1:
        return n
    else:
        global diepte
        diepte += 1
        print(diepte)
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
