count = 0

def mergeSort(arr):
    n=len(arr)
    if n < 2:
        return
    left=arr[:int(n/2)]
    right=arr[int(n/2):]

    #Recursive calls to the mergeSort method with smaller arrays
    mergeSort(left)
    mergeSort(right)

    #Call to the merge method to merge lists in sorted way
    return merge(left,right,arr)


def merge(left,right,arr):
    global count
    i=0
    j=0
    k=0
    x=len(left)
    y=len(right)
    while i < x and j < y:
        if left[i] < right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
            count = count + x-i
        k=k+1
    if i != x:
        while i < x:
            arr[k]=left[i]
            i=i+1
            k=k+1
    elif j != y:
        while j < y:
            arr[k]=right[j]
            j=j+1
            k=k+1
    return count


# arr=list(map(int,input("Enter the array: ").split()))
# print("Unsorted array: ", arr)
# mergeSort(arr)
# print("Sorted array: ", arr)
# print("No. of Inversions: ",count)
