def factorieel(n):
    if n == 1:
        return 1
    return n * factorieel(n - 1)


print(factorieel(5))
