# the update variable handle the case of given a sorted array or partially sorted
def BubbleSort(arr):
    # loop over the array and swap every two adjacent elements if the left > right
    for k in range(len(arr)):
        i = 0
        update = False
        # at the end of first loop is that the largest number is placed at the last index in the array
        # so in the next loop we go until len(arr) - finished elements 'k'
        while i < len(arr)-1-k:
            # print(i)
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                update = True
            i+=1
        if not update:  # if you go through a whole loop without swaping any elements then the array is sorted
            break
    return arr
    # print()
# print(arr)

arr2=[5,4,2,9,7,8,3,6,4,-1]
print (BubbleSort(arr2))
arr= [1,3,4,5,6,7,10]
print (BubbleSort(arr))