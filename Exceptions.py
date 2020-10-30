if __name__ == "__main__":

    for i in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(int(a/b))

        except ZeroDivisionError as e:
            print('Error Code: integer division or modulo by zero')

        except ValueError as e:
            print('Error Code:', e)
