import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

'''
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#We cannot plot multiple bar graph directly so we first create indexes using arange function of numpy
x_indexes = np.arange(len(ages_x))

#we will create a different width for each bar on x-axis
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

#Plotting bar chart
plt.bar(x_indexes - width, dev_y,width=width, color="#444444", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y,width=width, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y,width=width, color="#e5ae38", label="JavaScript")

plt.legend()

#to plot ages at x_indexes we use xticks
plt.xticks(ticks=x_indexes,labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()
'''

# Reading and plotting csv
df = pd.read_csv('C:/Users/ap644/Machine Learning/3. Matplotlib/developer.csv')
# It will create a list of columns
ids = df['Responder_id']
lang_responses = df['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()
