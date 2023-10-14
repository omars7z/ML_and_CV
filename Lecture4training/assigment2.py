import matplotlib.pyplot as plt

x = ["Category A", "Category B", "Category C", "Category D"]
y = [10, 25, 15, 30]

plt.bar(x, y, color='maroon', width=0.4)
plt.title('Bar Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

X = [1, 2, 3, 4, 5]
Y = [5, 7, 4, 2, 8]
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
