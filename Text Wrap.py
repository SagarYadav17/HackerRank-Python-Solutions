import textwrap


def wrap(string, max_width):
    wrap = textwrap.wrap(string, width=max_width)

    for i in range(0, len(wrap)):
        return '\n'.join(wrap[i:len(wrap)])


if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
