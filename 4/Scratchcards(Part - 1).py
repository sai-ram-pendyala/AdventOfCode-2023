with open('input.txt') as file:
    total = 0
    for line in file:
        card, nums = line.split(': ')
        _, cardId = card.split()
        winningNumbers, ourNumbers = nums.split(' | ')
        
        winningNumbers = set(map(int, winningNumbers.split()))
        ourNumbers = set(map(int, ourNumbers.split()))
        
        won = winningNumbers & ourNumbers

        if len(won) > 0:
            total += 2 ** (len(won) - 1)
    
    print(total)


