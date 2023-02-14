def Max(arr, start, end):
    """ Function to find the maximum value in an array
        Input:
            arr -> array of integers or floats
            start -> first index to start searching from it
            end -> last index to which stops searching
        Return:
            the maximum value in the array
    """
    mid = int((start + end) / 2)
    if (end - start) <= 1:
        return max(arr[start], arr[end])

    return max(Max(arr, start, mid), Max(arr, mid + 1, end))

def Min(arr, start, end):
    """ Function to find the minimum value in an array
            Input:
                arr -> array of integers or floats
                start -> first index to start searching from it
                end -> last index to which stops searching
            Return:
                the minimum value in the array
    """
    mid = int((start + end) / 2)
    if (end - start) <= 1:
        return min(arr[start], arr[end])

    return min(Min(arr, start, mid), Min(arr, mid + 1, end))



arr = [70, 250.4, 251.3, 50, 80, 140, 12, 14]

print(Max(arr, 0, len(arr)-1))
print(Min(arr, 0, len(arr)-1))
