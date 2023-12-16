from collections import deque

def bfs(mat, i, j, dirt):
    def isValid(i, j):
        return 0 <= i < len(mat) and 0 <= j < len(mat[0])

    def addNeighbor(i, j, dirt):
        if isValid(i, j) and (i, j, dirt) not in vis:
            q.append((i, j, dirt))
            vis.add((i, j, dirt))

    q = deque([(i, j, dirt)])
    vis = set()
    vis.add((i, j, dirt))
    eng = set()

    while q:
        i, j, dirt = q.popleft()
        eng.add((i, j))

        if mat[i][j] == '.':
            if dirt == 'l':
                addNeighbor(i, j - 1, dirt)
            elif dirt == 'r':
                addNeighbor(i, j + 1, dirt)
            elif dirt == 'u':
                addNeighbor(i - 1, j, dirt)
            elif dirt == 'd':
                addNeighbor(i + 1, j, dirt)

        elif mat[i][j] == '-':
            if dirt == 'l':
                addNeighbor(i, j - 1, dirt)
            elif dirt == 'r':
                addNeighbor(i, j + 1, dirt)
            else:
                addNeighbor(i, j - 1, 'l')
                addNeighbor(i, j + 1, 'r')

        elif mat[i][j] == '|':
            if dirt == 'u':
                addNeighbor(i - 1, j, dirt)
            elif dirt == 'd':
                addNeighbor(i + 1, j, dirt)
            else:
                addNeighbor(i - 1, j, 'u')
                addNeighbor(i + 1, j, 'd')

        elif mat[i][j] == '/':
            if dirt == 'l':
                addNeighbor(i + 1, j, 'd')
            elif dirt == 'r':
                addNeighbor(i - 1, j, 'u')
            elif dirt == 'd':
                addNeighbor(i, j - 1, 'l')
            else:
                addNeighbor(i, j + 1, 'r')

        else:
            if dirt == 'l':
                addNeighbor(i - 1, j, 'u')
            elif dirt == 'r':
                addNeighbor(i + 1, j, 'd')
            elif dirt == 'd':
                addNeighbor(i, j + 1, 'r')
            else:
                addNeighbor(i, j - 1, 'l')

    return len(eng)

with open('input.txt') as file:
    mat = []
    for line in file:
        mat.append(list(line.strip()))
    
    mx = float("-inf")

    for i in range(len(mat[0])):
        mx = max(mx, bfs(mat, 0, i, 'd'))

    for i in range(len(mat[0])):
        mx = max(mx, bfs(mat, len(mat) - 1, i, 'u'))

    for i in range(len(mat)):
        mx = max(mx, bfs(mat, i, 0, 'r'))

    for i in range(len(mat)):
        mx = max(mx, bfs(mat, i, len(mat[0]) - 1, 'l'))        
    
    print(mx)
