def quicksort(list):
    if list == []: 
        return []
    pivot = list[0]
    partition_1 = quicksort([x for x in list[1:] if x < pivot])
    partition_2 = quicksort([x for x in list[1:] if x >= pivot])
    return partition_1 + [pivot] + partition_2

l= [4,12,5,8,13]
print(quicksort(l))