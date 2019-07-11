
def buble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        else:
            continue
    return arr

print(buble_sort([1,4,3,2,1]))
            
