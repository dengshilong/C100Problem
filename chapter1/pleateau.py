# coding: utf-8


def pleateau(nums):
    length = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - length]:
            length += 1
    return length


def pleateaub(nums):
    length = 1
    i = 0
    while i + length < len(nums):
        if nums[i] == nums[i + length]:
            length += 1
        else:
            i += length
            while 0 < i < len(nums) and nums[i] == nums[i - 1]:
                i -= 1
    return length


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6]
    print(pleateau(nums))
    print(pleateaub(nums))
