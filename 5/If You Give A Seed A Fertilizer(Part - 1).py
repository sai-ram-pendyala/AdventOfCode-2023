with open('input.txt') as file:
    contents = []
    for line in file:
        contents.append(line.strip())

    seeds = []
    seedToSoil = []
    soilToFert = []
    fertToWater = []
    waterToLight = []
    lightToTemp = []
    tempToHum = []
    humToLoc = []

    mappings = {
        'seed-to-soil': seedToSoil, 
        'soil-to-fertilizer': soilToFert,
        'fertilizer-to-water': fertToWater,
        'water-to-light': waterToLight,
        'light-to-temperature': lightToTemp,
        'temperature-to-humidity': tempToHum,
        'humidity-to-location': humToLoc,
    }

    i = 0
    while i < len(contents):
        # print(contents[i])
        if contents[i].startswith('seeds:'):
            _, seeds = contents[i].split(': ')
            seeds = list(map(int, seeds.split()))
            # print(seeds)

        if contents[i].endswith('map:'):
            for k, v in mappings.items():
                if contents[i].startswith(k):
                    i += 1
                    while i < len(contents) and contents[i] != '':
                        destStart, sourceStart, ran = map(int, contents[i].split())
                        destEnd, sourceEnd = destStart + ran, sourceStart + ran 
                        v.append([sourceStart, sourceEnd, sourceStart - destStart])
                        i += 1
        
        i += 1

    finals = []
    transformations = [seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc]
    
    for seed in seeds:
        val = seed
        for transformation in transformations:
            for start, end, dif in transformation:
                if start <= val <= end:
                    val -= dif
                    break
        finals.append(val)
    
    print(min(finals))       