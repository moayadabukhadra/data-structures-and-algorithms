
def insertion_sort(arr):
    if type(arr)!= type([]):
        raise Exception("the input should be an array")
    if arr == []:
        raise Exception("the array is empty")
    i=1
    for i in range(len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and temp<arr[j]:
            arr[j + 1] = arr[j]
            j  = j - 1
        arr[j + 1] = temp
    return arr

print(insertion_sort([8,4,23,42,16,15]))