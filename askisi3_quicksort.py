def quicksort(l):
    if len(l) == 0:
        return

    pivot = l[-1]
    partition_1 = []
    partition_2 = []
    for i in range(len(l)):
        if l[i] < pivot:
            partition_1.append(l[i])
        else:
            partition_2.append(l[i])
    quicksort(partition_1)
    quicksort(partition_2)

l= [4,12,5,8,13]
quicksort(l)