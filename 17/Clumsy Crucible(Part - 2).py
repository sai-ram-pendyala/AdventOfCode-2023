import heapq

with open('input.txt') as file:
    mat = []
    for line in file:
        row = list(line.strip())
        mat.append(list(map(int, row)))

    R = len(mat)
    C = len(mat[0])
    Q = [(0, 0, 0, -1, -1)]
    D = {}

    while Q:
        dist, r, c, dir_, indir = heapq.heappop(Q)
        if (r, c, dir_, indir) in D:
            continue
        D[(r, c, dir_, indir)] = dist

        for i, (dr, dc) in enumerate([[-1,0], [0,1], [1,0], [0,-1]]):
            rr = r + dr
            cc = c + dc 
            newDir = i 
            newIndir = (1 if newDir != dir_ else indir + 1)
            if 0 <= rr < R and 0 <= cc < C and newIndir <= 10 and (newDir + 2) % 4 != dir_ and (newDir == dir_ or indir >= 4 or indir == -1):
                heapq.heappush(Q, (dist + mat[rr][cc], rr, cc, newDir, newIndir))
    
    ans = float("inf")
    for (r, c, dir_, indir), d in D.items():
        if r == R - 1 and c == C - 1:
            ans = min(ans, d)
    
    print(ans)
