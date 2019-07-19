# coding: utf-8

# 运算符优先级
ADD_SUB = 1
MUL_DIV = 2
BRACKET = 3


def polish(s):
    """将表达式转化成反向波兰式"""
    length = len(s)
    op = [''] * length
    code = [0] * length
    i = 0
    top = -1
    res = []
    cur = 0
    while i < length:
        if s[i].isalpha():
            res.append(s[i])
            i += 1
            continue
        elif s[i] == ' ':
            i += 1
            continue
        elif s[i] == '+' or s[i] == '-':
            cur = ADD_SUB
        elif s[i] == '*' or s[i] == '/':
            cur = MUL_DIV
        else:
            cur = BRACKET
        while top >= 0 and code[top] >= cur and code[top] != BRACKET:
            res.append(op[top])
            top -= 1
        if s[i] == ')':
            res.append(op[top])
            top -= 2
        else:
            top += 1
            op[top] = s[i]
            code[top] = cur
        i += 1
    while top >= 0:
        res.append(op[top])
        top -= 1
    return ''.join(res)


if __name__ == "__main__":
    assert polish('a+b*c') == 'abc*+'
    assert polish('a*b+c') == 'ab*c+'
    assert polish('a*(b+c)') == 'abc+*'
    assert polish('a*(b+c)-(e+f)/g') == 'abc+*ef+g/-'
    assert polish('a*(a/(b+c)*c)') == 'aabc+/c**'
