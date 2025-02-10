import numpy as np
import time

import matplotlib.pyplot as plt

# Number of variables
num_vars = 6

# Create a figure and polar subplot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Set the angle of each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The radar chart is a closed shape
angles += angles[:1]

# Function to update the radar chart
def update_chart(values):
    ax.clear()
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], ['North', 'North-East', 'South-East', 'South', 'South-West', 'North-West'])

    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.draw()
    plt.pause(0.1)

# Initial values
values = [1, 2, 3, 4, 5, 6]

# Live update loop
while True:
    values = np.random.randint(1, 10, size=num_vars).tolist()
    update_chart(values)
    time.sleep(1)