from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# slices = [60, 40, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37','#6d904f']

#Don't use pie chart if you have more than 5items in general

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

#if we want to create a slice of a particular language we use explode
explode = [0, 0, 0,0.1,0]
#To display percent we use autopct = '%1.1f%%'

plt.pie(slices, labels = labels, explode=explode, shadow=True,startangle=90,
        autopct = '%1.1f%%', wedgeprops={'edgecolor':'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f