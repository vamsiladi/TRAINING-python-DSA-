def selctionSort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
            (array[step],array[min_idx])=(array[min_idx],array[step])
data=[20,12,10,15,2]
size=len(data)
selctionSort(data,size)
print("sorted array in ascending order")
print(data)
