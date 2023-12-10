from collections import defaultdict, deque

with open('input.txt') as file:
    mat = []
    start = None
    
    for line in file:
        mat.append(list(line.strip('\n')))
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'S':
                start = [i, j]
                break
    
    # print(mat)

    adj = defaultdict(list)
    for i, row in enumerate(mat):
        print(row)
        for j, cell in enumerate(row):
            neighbors = []
            if cell == '|':
                neighbors = [(i-1, j), (i+1, j)]
            elif cell == "-":
                neighbors = [(i, j-1), (i, j+1)]
            elif cell == "L":
                neighbors = [(i-1, j), (i, j+1)]
            elif cell == "J":
                neighbors = [(i-1, j), (i, j-1)]
            elif cell == "7":
                neighbors = [(i+1, j), (i, j-1)]
            elif cell == "F":
                neighbors = [(i+1, j), (i, j+1)]
            elif cell == "S":
                start = (i, j)
            for x, y in neighbors:
                if x >= 0 and x < len(mat) and y >= 0 and y < len(row):
                    adj[(i, j)].append((x, y))
    
    startNei = []
    for x in adj:
        for y in adj[x]:
            if y == start:
                startNei.append(x)
    adj[start] = startNei
    # print(adj[start])

    INF = 1000000000
    dist = defaultdict(lambda: INF)
    q = deque()
    q.append(start)
    dist[start] = 0
    res = (0, start)
    # print(mat[start[0]][start[1]])

    while q:
        cur = q.popleft()
        print(cur, dist[cur])
        for nei in adj[cur]:
            if dist[nei] == INF:
                dist[nei] = dist[cur] + 1
                res = max(res, (dist[nei], nei))
                q.append(nei)
    
    print(res[0])