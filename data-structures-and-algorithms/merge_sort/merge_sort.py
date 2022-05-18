def Mergesort(arr):
    if type(arr)!= type([]):
        raise Exception("the input should be an array")
    if arr == []:
        raise Exception("the array is empty")
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        Mergesort(left)
        Mergesort(right)
        Merge(left, right, arr)


def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    while j < len(right):
        arr[k]=right[j]
        j += 1
        k += 1



if __name__=='__main__':
    arr=[5,12,7,5,5,7]
    Mergesort(arr)
    print(arr)