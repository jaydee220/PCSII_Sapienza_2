def CountingSort1(list):
    indexcount= [0]*100
    for i in list:
        indexcount[i]+=1
    print(*indexcount)



if __name__ == '__main__':

    _ =  input()
    ar = [int(i) for i in input().strip().split()]
    CountingSort1(ar)
