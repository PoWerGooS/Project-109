import csv
import pandas as pd
import random 
import statistics
import plotly.figure_factory as ff
diceResult = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)
mean = sum(diceResult)/len(diceResult)
standardDeviation = statistics.stdev(diceResult)
print(mean, standardDeviation)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)
print(mode, median)
fig = ff.create_distplot([diceResult], ["result"], show_hist = False)
fig.show()
