nums = {
        'one': '1' , 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
        }

with open(r'input.txt') as file:
    s = 0
    for line in file:
        digits = []
        
        for i in range(len(line)):
            if '1' <= line[i] <= '9':
                digits.append(line[i])
                continue
            
            for x in nums:
                if x == line[i: i+len(x)]:
                    digits.append(nums[x])
        
        print(line + ' ' + " ".join(digits))

        s += int(digits[0]+digits[-1])
    
    print(s)