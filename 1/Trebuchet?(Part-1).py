with open(r'input.txt') as file:
    s = 0
    for line in file:
        digits = []
        
        for char in line:
            if '0' <= char <= '9':
                digits.append(char)

        s += int(digits[0]+digits[-1])
    
    print(s)