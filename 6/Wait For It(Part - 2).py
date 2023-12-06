def binarySearch(l, h, dist, flag):
    res = -1
    time = h
    while l <= h:
        m = (l + h)//2
        if (time - m)*m > dist:
            res = m 
            if flag:
                h = m - 1
            else:
                l = m + 1
        else:
            if flag:
                l = m + 1
            else:
                h = m - 1

    return res

with open('sample.txt') as file:
    content = file.readlines()

    _, times = content[0].split(': ')
    _, dists = content[1].split(': ')

    time = int("".join(times.split())) 
    dist = int("".join(dists.split()))  

    mn = binarySearch(1, time, dist, True)
    mx = binarySearch(1, time, dist, False) 
    
    print(mx - mn + 1)