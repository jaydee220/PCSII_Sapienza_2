def CountingSort2(list):
    indexcount= [0]*100
    for i in list:
        indexcount[i]+=1
    return indexcount

def ReturnOrdered(arr):
    output = []
    for i in range(100):
        for j in range(arr[i]):
            output.append(i)
    return output

if __name__ == '__main__':

    m = input()
    ar = [int(i) for i in input().strip().split()]
    print (*printOrdered(CountingSort2(ar)))