if __name__ == '__main__':

    count_nmbr = int(input())
    nmbrs = sorted(list(map(int, input().split())))

    diff = nmbrs[1] - nmbrs[0]
    output = [nmbrs[0], nmbrs[1]]

    for id_nmbr in range(2, count_nmbr):
        newdiff = nmbrs[id_nmbr] - nmbrs[id_nmbr - 1]

        if newdiff == diff:
           output =  output + [nmbrs[id_nmbr - 1]] + [nmbrs[id_nmbr]]

        elif newdiff < diff:
            output = [nmbrs[id_nmbr - 1], nmbrs[id_nmbr]]
            diff = newdiff

    print(*output)
