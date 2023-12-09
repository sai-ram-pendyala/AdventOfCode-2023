from math import lcm

def getSteps(source, adj, instructions):
    i = 0
    cur = source
    steps = 0

    while True:
        if cur[-1] == 'Z':
            break
        if instructions[i] == 'L':
            cur = adj[cur][0]
        else:
            cur = adj[cur][1]

        steps += 1
        i = (i + 1)%(len(instructions) - 1)
    
    return steps


with open('input.txt') as file:
    content = file.readlines()
    instructions = content[0]
    # print(instructions)
    adj = {}
    starts = []
    for x in content[2:]:
        source, dests = x.strip('\n').split(' = ')
        dests = dests.strip('(')
        dests = dests.strip(')')
        left, right = dests.split(', ')
        adj[source] = [left, right]
        if source[-1] == 'A':
            starts.append(source)
    
    # print(starts)
    steps = []
    for x in starts:
        steps.append(getSteps(x, adj, instructions))
    
    print(lcm(*steps))

    # if len(steps) == 1:
    #     print(steps[0])
    # else:
    #     print(getSteps('AAA', adj, instructions))