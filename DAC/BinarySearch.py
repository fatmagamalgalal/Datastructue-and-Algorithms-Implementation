def BinarySearch(arr, element, start, end):
    if start >= end:
        if element == arr[start]:
            return start
        return -1

    mid = (start + end) // 2

    if element == arr[mid]:
        return mid
    elif element < arr[mid]:
        return BinarySearch(arr, element, start, mid - 1)
    return BinarySearch(arr, element, mid + 1, end)


def BinarySearch_iter(arr, element, start, end):
    mid = (start + end) // 2
    while start < end:
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            end = mid
        else:
            start = mid + 1
        mid = int((start + end) / 2)
    return -1


def test_BinarySearch(fn):
    arr = [1,3,4,5,6,7,10]
    print(fn(arr, 1, 0, len(arr)-1))
    print(fn(arr, 3, 0, len(arr) - 1))
    print(fn(arr, 4, 0, len(arr) - 1))
    print(fn(arr, 5, 0, len(arr) - 1))
    print(fn(arr, 6, 0, len(arr) - 1))
    print(fn(arr, 7, 0, len(arr) - 1))
    print(fn(arr, 10, 0, len(arr) - 1))
    print()
    print(fn(arr, 2, 0, len(arr) - 1))
    print(fn(arr, -1, 0, len(arr) - 1))
    print(fn(arr, 11, 0, len(arr) - 1))

# test_BinarySearch(BinarySearch_iter)

arr = [1,3,4,5,6,7,10]
test_BinarySearch(BinarySearch)

