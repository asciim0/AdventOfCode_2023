# AoC2023 - 2-2:

import re
import pandas as pd

inputfile = "input_2.txt"
elfRed = 12
elfGreen = 13
elfBlue = 14
score = 0
roundScore = 0 

with open(inputfile, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    
    # replaces ; with , only keeps draws in line
    line = line.replace(';',',')
    line.strip('Game *:')
    draws = re.sub(r'^.*?:', '', line)
    
    # read line into dataframe, remove linebreaks and only show max number per color
    df = pd.DataFrame([x.split(' ') for x in draws.split(',')])
    df.columns = ['','Number','Color']
    df['Number'] = pd.to_numeric(df['Number'])
    df['Color'] = df['Color'].str.replace('\n', '')
    df2 = df.groupby(['Color']).max(['Number'])

    # multiplies maxPulls and adds to overall score
    roundScore = (df2.loc["blue", "Number"]) * (df2.loc["green", "Number"]) * (df2.loc["red", "Number"]) 
    score = score + roundScore

print (score)

    
           
