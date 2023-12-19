# AoC2023 - 1-1: read line for line, combine first and last digit in each line into 2-figure number,
# add all numbers together

inputfile = "input_1-1.txt"
total = 0

with open(inputfile, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    num = []
    calval = ""
    
    # find digits in line and read into list
    for c in line:
        if c.isdigit():
            num.append(c)
            
    # if list is not empty, combine first and last number, add number to total
    if num:
        calval = (num[0]) + (num[-1])
        total = total + int(calval)
        
print ("Total value is: " + str(total))
    
