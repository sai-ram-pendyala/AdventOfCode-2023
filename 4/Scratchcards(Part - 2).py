from collections import defaultdict 

with open('input.txt') as file:
    total = 0
    cards = defaultdict(int)
    for line in file:
        card, nums = line.split(': ')
        _, cardId = card.split()
        cardId = int(cardId)
        winningNumbers, ourNumbers = nums.split(' | ')

        cards[cardId] += 1
        
        winningNumbers = set(map(int, winningNumbers.split()))
        ourNumbers = set(map(int, ourNumbers.split()))
        
        won = winningNumbers & ourNumbers
        # print(len(won))

        for i in range(cardId + 1, cardId + len(won) + 1):
            cards[i] += cards[cardId]
        
        # print(cards)

    print(sum(cards.values()))