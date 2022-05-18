# merge_sort

- Merge sort works by splitting the input list into two halves, repeating the process on those halves, and finally merging the two sorted halves together.

## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Sample Arrays

[8,4,23,42,16,15]

## Trace 

1. first we will split the array into two halves (left and right).

![split1](../data_structures_and_algorithms/images/merge_sort1.jpg)

2. we still have in each side more than one element , so we will keep spliting untill we have each element as right or left.

![sort2](../data_structures_and_algorithms/images/merge_sort2.jpg)


2. now we will merge the left and the right and sort them.

![sort3](../data_structures_and_algorithms/images/merge_sort3.jpg)

3. further merge and sort the left with right at the split before.

![sort4](../data_structures_and_algorithms/images/merge_sort4.jpg)

4. now we have the first half sorted we will repeat the same steps for the second half.

![sort5](../data_structures_and_algorithms/images/merge_sort5.jpg)

5. when we have the two halfes sorted we will mrge and sort them.

![sort6](../data_structures_and_algorithms/images/merge_sort6.jpg)



