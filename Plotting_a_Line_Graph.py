"""Generating Data"""

# Importing Matplotlib
import matplotlib.pyplot as plt


"""Plotting a simple line graph"""

squares = [1, 4, 9, 16, 25]

# This function can generate one or more plots in the same figure
fig, ax = plt.subplots()
ax.plot(squares)

# Opens Matplotlib's viewer and displays the plot
# Uncomment line 16 to display example 1 and comment it out after viewing to view example 2
#plt .show()

"""Changing the label type and line thickness"""

ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of thick label
ax.tick_params(axis='both', labelsize=14)

# Uncomment line 31 to display example 2 and comment it out after viewing to view example 3
#plt.show()

"""Correcting the plot"""

# Did you notice that the Values started at 0.0 ?
# we need to change that to start from 1.0

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Removing default value and setting user generated value
ax.plot(input_values, squares)

# Uncomment line 45 to display example 3 and comment it out after viewing to view example 4
# plt .show()

"""Using built-in styles"""

# Run on you command line to see what styles are available on you system
# import matplotlib.pyplot as plt
# plt.style.available

# Use any of the options to design your graph
plt.style.use('dark_background')

plt .show()








