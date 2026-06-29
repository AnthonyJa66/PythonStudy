a = 100
b = 200
c=1

def sum():
    global c
    c += a
    d = a + b
    return c + d


x = a + 1

print(sum())
print(c)
print(b)
