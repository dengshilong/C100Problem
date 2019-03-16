# coding: utf-8

"""
可以用变量prefix来表示前置和，用suffix来表示后置和，
用i表示前置和累加元素的位置，i从前往后加，用j表示后置和累加元素的位置, j从后往前加。
当prefix > suffix时，累加后置和，也就是j向前走；
当prefix < suffix时，累加前置和，也就是i往后走；
当prefix == suffix时，同时累加前置和与后置和，也就是i往后走，j往前走
public class HeadTail {
"""

def head_tail(nums):
    i = 0
    j = len(nums) - 1
    prefix = 0
    suffix = 0
    result = 0
    while i < len(nums) and j >= 0:
        if prefix == suffix:
            prefix += nums[i]
            suffix += nums[j]
            i += 1
            j -= 1
            result += 1
        elif prefix > suffix:
            suffix += nums[j]
            j -= 1
        else:
            prefix += nums[i]
            i += 1
    return result


if __name__ == "__main__":
    nums = [3, 6, 2, 1, 4, 5, 2]
    print(head_tail(nums))
