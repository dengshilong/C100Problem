# coding: utf-8

def bad_index_search(x):
    index = -1
    for i in range(0, len(x)):
        if x[i] == i + 1:
            index = i + 1
            break
    return index


def index_search(x):
    low = 0
    high = len(x) - 1
    mid = int((high - low) / 2 + low / 2)
    index = -1
    while low <= high:
        if x[mid] > mid + 1:
            low = mid + 1
        elif x[mid] < mid + 1:
            high = mid - 1
        else:
            index = mid + 1
            break
    return index

if __name__ == "__main__":
    x = [-2, -1, 3, 7, 8]
    print(bad_index_search(x))
    print(index_search(x))