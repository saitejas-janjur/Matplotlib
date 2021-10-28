import matplotlib.pyplot as plt

# x_values will be every number from 1 - 1000
x_values = [1, 2, 3, 4, 5]
# y_values will be the square of all the values in x_values
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Calling the scatter function
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
