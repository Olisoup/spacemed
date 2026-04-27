# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-computelab-2025-2]
#     language: python
#     name: conda-env-conda_envs-computelab-2025-2-py
# ---

# %% [markdown]
# # Loading Data

# %% [markdown]
# ## 1. Data
# ### Getting Data

# %%
time = []  # We are creating lists to read the different columns
absorption = [] 

# %%
dataFile = open('data/pulse_data.csv','r') # Command to open the datafile and name it

# %%
dataFile.readline() # Read the first line before the for loop which then throws it away
for line in dataFile.readlines():
    line = line.split(",") # We want to split the lines and delimiting them with the "," 
    time.append(float(line[0])) # Anything before the comma is "imte" 
    absorption.append(float(line[1])) # Anything after is "absorption"

# %%
print(len(time), len(absorption)) # View length of the data set (make sure to restart kernel as needed)

# %%
for i in range (10):
    print(time[i], absorption[i]) # Printing the first 10 lines

# %%
import numpy # Numerical Python
from matplotlib import pyplot # Extension that makes it look like matlab in a sense

# %%
# Create random normal datapoints on both axes
x=numpy.random.normal(size=(500,))
y=numpy.random.normal(size=(500,))

# %%
pyplot.plot(x,y,'.m') # .m disconnects the lines and makes them magenta
pyplot.xlabel("random x") # always label your axes
pyplot.ylabel("random y")
pyplot.title("random number generator") # always name your baby -> Give it a title

# %%
# Help Command
# pyplot.plot?

# %%
pyplot.plot(time,absorption,'m') # Doing it with our actual data, keeping linked because it looks nicer
pyplot.xlabel("Time (s) ")
pyplot.ylabel("Absorption")
pyplot.title("Absorption vs Time")

# %% [markdown]
# ## 2. Messing around

# %%
pyplot.plot(absorption,'m') # Only using the absorption seems to put the number of samples as the default x which makes sense
pyplot.xlabel("Samples")
pyplot.ylabel("Absorption")
pyplot.title("Absorption vs Samples")

# %%
pyplot.scatter(time,absorption) # Not sure how to get a scatter plot to work, will see this weekend
pyplot.xlabel("Time")
pyplot.ylabel("Absorption")
pyplot.title("Absorption vs Time")

# %%
import matplotlib.pyplot as plt #Testing different types of plots and seeing what the numbers modify
import numpy as np

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(15, 190, len(x))
colors = np.random.uniform(15, 50, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
