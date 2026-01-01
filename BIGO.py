def multiplynum(n):
    return n*n
print(multiplynum(10))

def print_item(n):
    for i in range(n):
        print(i)
print_item(2)


def print_item(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_item(10)

def print_item(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
print_item(10)

def print_item(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_item(10)