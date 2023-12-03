from functools import reduce

def getNumber(schema, i, j):
    
    while j - 1 >= 0 and schema[i][j-1].isdigit():
        j -= 1
    
    num = ''
    while j + 1 < len(schema[0]) and schema[i][j+1].isdigit():
        num += schema[i][j]
        schema[i][j] = '.'
        j += 1
    
    num += schema[i][j]
    schema[i][j] = '.'
    
    return int(num)

with open('input.txt') as file:
    schema = []
    for line in file:
        cur = list(line)
        if cur[-1] == '\n':
            schema.append(cur[:-1])
        else:
            schema.append(cur)

    gears = []
    for i in range(len(schema)):
        for j in range(len(schema[0])):
            if schema[i][j] == '*':
                gears.append([i, j])
    # print(gears)

    total = 0
    for x, y in gears:
        neighbors = set()
        for i, j in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1], [x - 1, y - 1], [x - 1, y + 1], [x + 1, y - 1], [x + 1, y + 1]]: 
            if 0 <= i < len(schema) and 0 <= j < len(schema[0]) and schema[i][j].isdigit():
                neighbors.add(getNumber(schema, i,j))

        if len(neighbors) == 2:
            neighbors = list(neighbors)
            total += neighbors[0] * neighbors[-1]
    
    print(total)