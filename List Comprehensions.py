if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    a = []

    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                if x + y + z != n:
                    a.append([x, y, z])

    print(a)
