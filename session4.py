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
import numpy # Numerical Python
from matplotlib import pyplot # Extension that makes it look like matlab in a sense

# %%
pyplot.plot(time,absorption,'m') # Doing it with our actual data, keeping linked because it looks nicer
pyplot.xlabel("Time (s) ")
pyplot.ylabel("Absorption")
pyplot.title("Absorption vs Time")
