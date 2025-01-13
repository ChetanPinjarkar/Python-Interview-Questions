def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


arr = [2,1,5,7,4]
print(bubble_sort(arr))
