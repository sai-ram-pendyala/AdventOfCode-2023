with open('input.txt') as file:
    content = file.readlines()
    instructions = content[0]
    # print(instructions)
    adj = {}
    for x in content[2:]:
        source, dests = x.strip('\n').split(' = ')
        dests = dests.strip('(')
        dests = dests.strip(')')
        left, right = dests.split(', ')
        adj[source] = [left, right]
    
    # print(adj)

    i = 0
    cur = 'AAA'
    count = 0

    while True:
        if cur == 'ZZZ':
            break
        # print(i, instructions[i])
        if instructions[i] == 'L':
            cur = adj[cur][0]
        else:
            cur = adj[cur][1]
        # print(cur)


        count += 1
        i += 1
        if i == len(instructions) - 1:
            i = 0
    
    print(count)
