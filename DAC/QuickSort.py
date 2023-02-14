def Partition(arr, start, end):
    pivot = start
    start += 1
    # divide the array into two sub arrays where:
    # the left array is smaller than the pivot
    # the right array is larger than the pivot
    while start <= end:
        # go through with two pointers that swap two elements to make them in the right side
        # 'smaller than the pivot in the right & larger than the pivot on the left'
        # [18,12,18,  26  ,6,15,9,30,1,500,0,22,  14  ] swap 26 and 14
        if arr[start] > arr[pivot] and arr[end] < arr[pivot]:
            # print(arr[start], arr[end])
            arr[start], arr[end] = arr[end], arr[start]
        # move the pointers forward
        if arr[start] <= arr[pivot]:
            start += 1
        if arr[end] >= arr[pivot]:
            end -= 1
    # print('array before swap', arr)  # [18   , 12, 18, 14, 6, 15, 9, 0,   1   , 500, 30, 22, 26]
    # after finishing.. swap the pivot and the high --> swap 18 and 1
    arr[end], arr[pivot] = arr[pivot], arr[end]
    print('finished partition')
    return end

def QuickSort(arr, start, end):

    if start >= end:
        return

    loc = Partition(arr, start, end)

    QuickSort(arr, start, loc-1)
    QuickSort(arr, loc+1, end)

    # no need to merge because the swap in the original array itself




arr = [18,12,18,26,6,15,9,30,1,500,0,22,14]
# print(arr)
# print(Partition(arr,0,len(arr)-1))
# print(arr)
QuickSort(arr, 0,len(arr)-1)
print(arr)
