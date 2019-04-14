# coding: utf-8


def reverse(nums, begin, end):
    while begin < end:
        nums[begin], nums[end] = nums[end], nums[begin]
        begin += 1
        end -= 1


def permutation(n):
    nums = [i for i in range(1, n + 1)]
    return iteration_permutation(nums)


def iteration_permutation(nums):
    """求有序数组的全排列"""
    result = []
    length = len(nums)
    while True:
        result.append(''.join(str(i) for i in nums))
        i = length - 2
        while i >= 0 and nums[i] > nums[i + 1]:
            i -= 1
        if i < 0:
            break
        j = length - 1
        while j > i and nums[i] > nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i + 1, length - 1)
    reverse(nums, 0, length - 1)   # 将有序数组还原
    return result


if __name__ == "__main__":
    s = permutation(4)
    for item in s:
        print(item)