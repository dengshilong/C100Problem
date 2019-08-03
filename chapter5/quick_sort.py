# coding: utf-8


def partition(x, left, right):
    pivot = x[right]
    index = left
    for i in range(left, right):
        if x[i] < pivot:
            x[i], x[index] = x[index], x[i]
            index += 1
    x[index], x[right] = x[right], x[index]
    return index


def quick_sort(x):
    _quick_sort(x, 0, len(x) - 1)


def _quick_sort(x, left, right):
    if left >= right:
        return
    index = partition(x, left, right)
    _quick_sort(x, left, index - 1)
    _quick_sort(x, index + 1, right)



if __name__ == "__main__":
    x = [7, 6, 2, 3, 4, 1]
    quick_sort(x)
    assert x == [1, 2, 3, 4, 7]
    x = [7, 6, 5, 4]
    quick_sort(x)
    assert x == [4, 5, 6, 7]
