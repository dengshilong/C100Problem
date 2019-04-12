# coding: utf-8


def reverse(nums, begin, end):
    while begin < end:
        nums[begin], nums[end] = nums[end], nums[begin]
        begin += 1
        end -= 1


def permutation(n):
    nums = [i for i in range(1, n + 1)]
    result = []
    _recursion_permutation(nums, 0, result)
    return result


def _recursion_permutation(nums, start, result):
    if start == len(nums) - 1:
        result.append(''.join([str(i) for i in nums]))
        return
    i = len(nums)
    while i > start:
        _recursion_permutation(nums, start + 1, result)
        nums[start], nums[i - 1] = nums[i - 1], nums[start]
        i -= 1
        if i <= start:
            break
        reverse(nums, start + 1, len(nums) - 1)


if __name__ == "__main__":
    s = permutation(4)
    for item in s:
        print(item)
