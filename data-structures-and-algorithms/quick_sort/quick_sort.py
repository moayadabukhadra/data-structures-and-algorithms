def quick_sort(arr,left,right):
    if type(left) is not int:
        raise Exception("left must be int")
    if type(right) is not int:
        raise Exception("right must be int")

    if type(arr) is not list:
        raise Exception("Input must be a list")
    if left < right:
        position= Partition(arr,left,right)

        quick_sort(arr, left, position - 1)

        quick_sort(arr, position + 1, right)



def Partition(arr, left, right):
    pivot =  arr[right]

    low = left - 1
    for i  in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
    swap(arr, right, low + 1)
    return low + 1

def swap(arr, i, low):
    temp= arr[i]
    arr[i]=arr[low]
    arr[low]=temp


if __name__=="__main__":
    arr=[8,4,23,42,16,15]
    quick_sort(arr,0,len(arr)-1)
    print(arr)
