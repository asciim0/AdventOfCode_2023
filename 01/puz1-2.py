# AoC2023 - 1-1: read line for line, combine first and last digit in each line into 2-figure number,
# add all numbers together - but this time, numbers can be written out as well

import re

inputfile = "input_1-1.txt"

numbers = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
total = 0

# finds all written out numbers in line, returns position and digit in dictionary
def find_textnumbers(text):
    valdict={}
    for i, j in numbers.items():
        if (text.find(i) >= 0):
            keys = [m.start() for m in re.finditer(i, text)]
            for key in keys:
                valdict[key]=j
    return valdict

# finds all digits in line, returns position and digit in dictionary
def find_digitnumbers(text):
    valdict2={}
    testkey = [m.start() for m in re.finditer(r'[0-9]', text)]
    testval = re.findall(r'[0-9]', text)
    valdict2 = dict(map(lambda i,j : (i,j) , testkey, testval))
    return valdict2

with open(inputfile, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    # nums is dictionary of position i and number j, calval is calibration value as per exercise
    nums = {}
    calval = ""
    nums = find_textnumbers(line)
    nums.update(find_digitnumbers(line))

    # sorts values by index, takes first and last to form 2 digit number as calval
    myKeys = list(nums.keys())
    myKeys.sort()
    sorted_dict = {i: nums[i] for i in myKeys}
    values = list(sorted_dict.values())    
    first_key = values[0]
    last_key = values[-1]  
    calval = (str(first_key + last_key))
    
    # updates total for all 1000 lines
    total = total + int(calval)
        
print ("Total value is: " + str(total))

