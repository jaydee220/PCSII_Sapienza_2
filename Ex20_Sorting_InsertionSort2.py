
def insertionSort(arr):
    length = len(arr)

    for i in range(length-1):
        #check if is already sorted
        if arr[i]<arr[i+1]:
            print (*arr)
            continue
        #if not take the fragment and sort it
        elif arr[i]>arr[i+1]:
            new = sorted(arr[:i+2])
            arr = new + arr[i+2:]
            print (*arr)

if __name__ == '__main__':

    m = input()
    ar = [int(i) for i in input().strip().split()]
    insertionSort(ar)
