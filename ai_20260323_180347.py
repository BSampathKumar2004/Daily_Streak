 Here's a simple example of the QuickSort algorithm in Python. Note that this version assumes the list to be sorted is already defined and does not handle edge cases such as an empty list or a list with one element.

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

You can use this function to sort a list like so:

```python
print(quicksort([3,6,8,9,1,2,5]))  # Output: [1, 2, 3, 5, 6, 8, 9]
```