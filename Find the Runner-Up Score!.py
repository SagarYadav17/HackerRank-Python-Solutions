if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    a = list(arr)
    m = max(a)

    new_list = []

    for i in range(len(a)):
        if m != a[i]:
            new_list.append(a[i])

    y = max(new_list)

    print(y)
