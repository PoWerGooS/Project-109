import csv
import pandas as pd
import random 
import statistics
import plotly.figure_factory as ff
df = pd.read_csv("exams.csv")
heightList = df["math score"].to_list()
weightList = df["gender"].to_list()
mean = statistics.mean(heightList)
median = statistics.median(heightList)
mode = statistics.mode(heightList)
standardDeviation = statistics.stdev(heightList)
fig = ff.create_distplot([heightList], ["math score"], show_hist = False)
fig.show()
#print(mean, median, mode, standardDeviation)
heightoneDstart, heightoneDend = mean-standardDeviation, mean+standardDeviation
heighttwoDstart, heighttwoDend = mean-(2*standardDeviation), mean+(2*standardDeviation)
heightthreeDstart, heightthreeDend = mean-(3*standardDeviation), mean+(3*standardDeviation)
heightListoneD = [result for result in heightList if result > heightoneDstart and result < heightoneDend]
print(len(heightListoneD))
print(len(heightListoneD)*100/len(heightList))
heightListtwoD = [result for result in heightList if result > heighttwoDstart and result < heighttwoDend]
print(len(heightListtwoD)*100/len(heightList))
heightListthreeD = [result for result in heightList if result > heightthreeDstart and result < heightthreeDend]
print(len(heightListthreeD)*100/len(heightList))