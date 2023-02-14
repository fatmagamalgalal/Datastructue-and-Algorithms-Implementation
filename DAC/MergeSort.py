def fill(resarr, arr):
    for i in arr:
        resarr.append(i)

def merge(arr, arr1, arr2):  # merge two sorted arrays
    i=j=k=0
    # go through the two arrays with two pointers and append the min value first
    while i < len(arr1):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j += 1
            if j >= len(arr2):
                break
        k+=1
    # append the rest of the two arrays 'when one array ends before the other'
    if len(arr1) > 0:
        fill(arr, arr1)
    if len(arr2) > 0:
        fill(arr, arr2)


def MergeSort(arr):
    # retrn when there is only 1 or no element in the sub array
    if len(arr) <= 1:
        return

    # divide the array into two sub arrays
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    # sort each sub array
    MergeSort(left)
    MergeSort(right)

    # merge the two returned sub arrays
    merge(arr, left, right)


arr = [18,12,18,26,6,15,9,30,22,14]
MergeSort(arr)
print(arr)