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

    times = list(map(int, times.split())) 
    dists = list(map(int, dists.split())) 

    res = 1

    for i in range(len(times)):
        mn = binarySearch(1, times[i], dists[i], True)
        mx = binarySearch(1, times[i], dists[i], False) 
        res *= mx - mn + 1
    
    print(res)