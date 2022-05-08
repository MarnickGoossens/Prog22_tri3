def gemene_deler(x, y):
    if y == 0:
        return x
    else:
        return gemene_deler(y, x % y)


print(gemene_deler(4, 8))
