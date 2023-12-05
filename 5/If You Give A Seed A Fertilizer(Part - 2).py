def finds(transformations, loc):
    val = loc 
    l = 0
    for transformation in transformations[::-1]:
        for start, end, dif in transformation: 
            if start <= val <= end:
                l += 1
                val += dif
                break
    if l == len(transformations):
        return val
    else:
        return None

def findInSeeds(seeds, loc):
    for start, end in seeds:
        if start <= loc <= end:
            return True
    return False


with open('sample.txt') as file:
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
        if contents[i].startswith('seeds:'):
            _, ranges = contents[i].split(': ')
            ranges = list(map(int, ranges.split()))

            for i in range(0, len(ranges), 2):
                start = ranges[i]
                end = start + ranges[i + 1]
                seeds.append([start, end])
        
        if contents[i].endswith('map:'):
            for k, v in mappings.items():
                if contents[i].startswith(k):
                    i += 1
                    while i < len(contents) and contents[i] != '':
                        destStart, sourceStart, ran = map(int, contents[i].split())
                        destEnd, sourceEnd = destStart + ran, sourceStart + ran 
                        v.append([destStart, destEnd, sourceStart - destStart])
                        i += 1
        i += 1

    finals = []
    transformations = [seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc]
    
    print(transformations[::-1])

    loc = 0
    while True:
        m = finds(transformations, loc)  
        if m != None:
            print(loc)
            if findInSeeds(seeds, m):
                print(loc)
                break
            else:
                loc += 1
        else:
            loc += 1