def quickSort1(list):
    pivot = list[0]
    left = []
    right = []
    equal = []
    for i in range(0, len(list)):
        if (list[i] > pivot):
            right.append(list[i])
        elif (list[i] < pivot):
            left.append(list[i])
        else:
            equal.append(list[i])
    output = left + equal + right
    print(*output)


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
quickSort1(ar)
