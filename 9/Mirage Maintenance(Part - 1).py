with open('input.txt') as file:
    res = 0
    for line in file:
        nums = list(map(int, line.split()))
        steps = [nums]
        while not all([x == 0 for x in steps[-1]]):
            step = []
            for i in range(1, len(steps[-1])):
                step.append(steps[-1][i] - steps[-1][i-1])
            steps.append(step[:])
        
        steps[-1].append(steps[-1][-1])

        for i in range(len(steps) - 1, 0, -1):
            steps[i - 1].append(steps[i - 1][-1] + steps[i][-1])

        res += steps[0][-1]

    print(res)        