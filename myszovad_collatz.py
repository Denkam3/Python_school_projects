import matplotlib.pyplot as plt
import numpy as np

def collatz(number):
    # Algorithm for Collatz conjecture
    steps = 0
    max_value = number
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        steps +=1
        max_value = max(max_value, number)
    return steps, max_value

limit = 1_000_000

# Generate vectors to save data for plot
steps = np.zeros(limit)
max_values = np.zeros(limit)

# Check all numbers
for i in range(1, limit + 1):
    steps[i - 1], max_values[i - 1] = collatz(i)

fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (13,6))

# Histogram plot
axs[0].hist(steps, bins = 250)
axs[0].set_xlabel("Number of steps")
axs[0].set_ylabel("Frequency")
axs[0].set_title("Histogram - number of steps")

# Plot steps

# Plot max value for every number
x = np.arange(0, limit)

axs[1].plot(x, max_values)
axs[1].set_xlabel("Number")
axs[1].set_ylabel("Maximum value")
axs[1].set_title("Graph of max value reached for each number")

plt.show()
