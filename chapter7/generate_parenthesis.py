# coding: utf-8

"""
假设还有left个左括号和right个右括号等待匹配，根据left与right的大小可以分三种情况
1.当 left == right 时，此时只能继续放左括号
2.当 left < right时，可以有两个选择， 继续放一个左括号或者继续放一个右括号。
放左括号时需要判断left是否大于0，只有left大于0时,才能继续放左括号。
放右括号时则不需要判断。
3.当left > right时，此时没有意义。
"""


def generate_parenthesis(n):
    result = []
    _generate_parenthesis(n, n, n, "", result)
    return result


def _generate_parenthesis(left , right, n, s, result):
    if len(s) == n * 2:
        result.append(s)
    else:
        if left == right:
            _generate_parenthesis(left - 1, right, n, s + '(', result)
        elif (left < right):
            if left > 0:
                _generate_parenthesis(left - 1, right, n, s + "(", result)
            _generate_parenthesis(left, right - 1, n, s + ")", result)


if __name__ == "__main__":
    print(generate_parenthesis(2))
    print(generate_parenthesis(3))