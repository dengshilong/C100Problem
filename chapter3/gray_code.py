# coding: utf-8


def gray_code(n):
    result = []
    if n == 0:
        result.append('')
    else:
        temp = gray_code(n - 1)
        for item in temp:
            result.append('0' + item)
        for i in range(len(temp)):
            result.append('1' + temp[len(temp) - i - 1])
    return result


if __name__ == "__main__":
    print(gray_code(3))
