
def insertionSort(ar):
    length = len(ar)
    s_obj = ar[-1]
    for ind in reversed(range(length-1)):
        if s_obj < ar[ind]:
            ar[ind+1] = ar[ind]
            print (*ar)
        elif s_obj > ar[ind]:
            ar[ind+1] = s_obj
            print(*ar)
            break
    if s_obj < ar[0]:
        ar[0] = s_obj
        print (*ar)

if __name__ == '__main__':

    m = input()
    ar = [int(i) for i in input().strip().split()]
    insertionSort(ar)
