games = {}

with open(r'input.txt') as file:
    for line in file:
        game, balls = line.strip().split(': ')
        gameId = game.split()
        gameId = gameId[1]
        rounds = balls.split('; ')
        for i in range(len(rounds)):
            round = rounds[i].split(', ')
            freq = {}
            for x in round:
                count, color = x.split()
                if color in freq:
                    freq[color] += count 
                else:
                    freq[color] = count
            rounds[i] = freq
        
        games[gameId] = rounds
    
    power = 0
    for id, rounds in games.items():
        mxCount = {}
        for round in rounds:
            for color, count in round.items():
                if color in mxCount:
                    mxCount[color] = max(mxCount[color], int(count))
                else:
                    mxCount[color] = int(count)
        
        power += mxCount['red'] * mxCount['green'] * mxCount['blue'] 
    
    print(power)