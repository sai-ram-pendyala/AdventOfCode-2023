mat  = []
galaxies = []
emptyRows = set()
emptyCols = set()

with open('input.txt') as file:
    for line in file:
        mat.append(list(line.strip()))
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '#':
                galaxies.append((i, j))
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '#':
                break
        else:
            emptyRows.add(i)
    
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if mat[j][i] == '#':
                break
        else:
            emptyCols.add(i)
    
    dist = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i] 
            x2, y2 = galaxies[j]
            mnX = min(x1, x2)
            mxX = max(x1, x2)
            mnY = min(y1, y2)
            mxY = max(y1, y2)
            x, y = 0, 0
            for p in range(mnX + 1, mxX + 1):
                if p in emptyRows:
                    x += 1000000
                else:
                    x += 1
            for q in range(mnY + 1, mxY + 1):
                if q in emptyCols:
                    y += 1000000
                else:
                    y += 1
            # print(galaxies[i], galaxies[j], x, y)
            dist += x + y 
    
    print(dist)
    
