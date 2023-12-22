# AoC2023 - 2-1:

# 12 red cubes, 13 green cubes, and 14 blue

import re
import pandas as pd

inputfile = "input_2.txt"
elfRed = 12
elfGreen = 13
elfBlue = 14
score = 0
 

with open(inputfile, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    
    # replaces ; with , and extracts gamenumber, only keeps draws in line
    line = line.replace(';',',')
    gameNumber = int(' '.join(re.findall(r"(\d+):", line)))
    line.strip('Game *:')
    draws = re.sub(r'^.*?:', '', line)
    
    # read line into dataframe, remove linebreaks and only show max number per color
    df = pd.DataFrame([x.split(' ') for x in draws.split(',')])
    df.columns = ['','Number','Color']
    df['Number'] = pd.to_numeric(df['Number'])
    df['Color'] = df['Color'].str.replace('\n', '')
    df2 = df.groupby(['Color']).max(['Number'])
    
    # compare max number to max elf numbers - if won, add gameID to score
    if ((df2.loc["blue", "Number"]) <= elfBlue) and ((df2.loc["green", "Number"]) <= elfGreen) and ((df2.loc["red", "Number"]) <= elfRed):
        score = score + gameNumber

print (score)

    
           