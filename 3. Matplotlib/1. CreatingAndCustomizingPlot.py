#importing module
from matplotlib import pyplot as plt

#Adding style to graph
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

# We can have comic like stlye by using xkcd
plt.xkcd()

# Median Developer Salaries by Age
Ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


#Adding colors and line type using format string syntax '[marker][color][line]'
plt.plot(Ages_x,dev_y,'.--',label = 'All Devs')       #ploting the list
#Another way
#plt.plot(Ages_x,dev_y,color='#444444',linestyle = '--',marker ='.',label = 'All Devs') #Here we can use hexvalues for color


#Adding another graph
# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(Ages_x,py_dev_y,'ob-',linewidth = '3',label = 'Python')  #To make line thick use linewidth
#Another way
#plt.plot(Ages_x,py_dev_y,color ='b',linestyle = '-',marker='o',label = 'Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(Ages_x,js_dev_y,color ='#adad3b',linewidth = 3,label = 'Javascript')


plt.xlabel('Ages')          #Adding label to x-axis
plt.ylabel('Median Salary in (USD)')   #Adding label to y-axis
plt.title('Median Developer Salaries by Age')

#Adding legends to graph so we can distingiush the graph
plt.legend()                #showing the graph

#Adding grid to graph
plt.grid(True)

#If we are having some padding issue then we can use 
plt.tight_layout()  #It will automatically adjust the line graph

#To save the plot
plt.savefig('plot.png')  #It will saved in current directory

plt.show()