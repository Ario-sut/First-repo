def minmax(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i 

    for i in arr:
        if i > max:
            max = i
    result = sum(arr) - min, sum(arr) - max
    return result



print(minmax([1,4,7,9,8]))