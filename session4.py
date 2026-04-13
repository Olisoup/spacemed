# ---
# title: "Session 4: Reproducible Documents"
# author: Joseph Carol
# format:
#   html:
#     code-fold: true
#   pdf:
#     echo: false
#     pdf-engine: pdflatex
#     toc: true
#     number-depth: 2
#     number-sections: true
#     papersize: a4
#     documentclass: article
# jupyter: python3
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
# # Session 4
# ## Reproducible Documents and Algorithm Design

# %% [markdown]
# LET'S GET GOING WITH SOME LATEX IN MD :)))))

# %% [markdown]
# ## Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# _constant mass flow rate_ $R$ meassured in kg/s
# and _exhaust velocity relative to the rocket_
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$ {#eq-rocket-acc}
# Integrating both sides of @eq-rocket-acc from 0
# to $T$ we get

# %% [markdown]
# ### Load Data

# %%
# Create two lists that will contain the two separate values in the table

time = []
absorption = []

# %%
# Import the file

dataFile = open("data/pulse_data.csv")

# Use a for loop to fill the lists

dataFile.readline() # We don't want to read in the first row because it's just the column headers, so we read through the first line to "trash" it

for line in dataFile.readlines(): # Run a for loop through all rows of the file (with the exception of the first one cause we already ditched it)
    line = line.split(",") # Split into two lists with the "," delimeter
    time.append(float(line[0])) # Add to the time list
    absorption.append(float(line[1])) # Add to the absorption list

# %%
# First important to import your libraries

import numpy
from matplotlib import pyplot as plt

# %% [markdown]
# ## Data Visualisation

# %%
# TELL QUARTO WHAT TO DO WITH THIS FIGURE FOR PDF VIEWING

#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"

# Create a plot using the 'time' and 'absorption' lists created earlier

plt.plot(time, absorption)
plt.title("Sample Absorption vs. Time for a .tar Pulse Data File")
plt.xlabel("Time (s)")
plt.ylabel("Absorption (unknown units)")

# %% [markdown]
# ## Lists and Arrays Intro

# %%
a = numpy.arange(10)+1

# %%
a.shape

# %%
a.dtype

# int64 means each integer require 64 bits of storage

# %%
a.nbytes

# there are 8 bits in a byte

# %%
b = numpy.array([[1,2,3], [4,5,6]])
b

# %%
b.shape

# %%
b.T # Transpose function -- rotates the array 90 degrees

# %%
b.T @ b # @ is dot product, so this is the b-matrix squared

# %%
a

# %%
print(numpy.max(a)) # finds the maximum value in an array
print(numpy.argmax(a)) # tells you what index the maximum value is at

# %% [markdown]
# ## Algorithm Design

# %% [markdown]
# We want to find the heart rate using HR = 60/deltaTpeaks

# %%
# Show one cycle of the PPG data

plt.plot(time, absorption, ".")
plt.xlim(time[30], time[250])

# %% [markdown]
# We want to be able to calculate the heart rate using a primitive technique (meaning no automatic functions). So let's try using a for loop that finds the global maximum of each cycle using a window!

# %%
absorption = numpy.array(absorption) # Turn the list into a numpy array
time = numpy.array(time)
# subset = absorption[:1000] # Just take a subset to make initial testing easier
subset = absorption
w = 50 # Window for finding global maxmimum
plt.plot(subset)

# %%
peaks = [] # Create a new array to store the peak locations

# Create a for loop that will use a sliding window of size 2w to find the global maxima for each cycle
for i in range(len(subset)):
    start = max(i-w, 0) # Start the window at i-w unless that is negative, in which case start at 0
    end = min(i+w, len(subset)) # Stop the window at i+w unless that is greater than the length of the list, in which case end at the end
    window = subset[start:end] # Get the window
    max_pos = numpy.argmax(window) + start # Gives us the position of where the maximum lies within the for loop window.
        # "+ start" is needed in order to SHIFT the index of the position back to where it is in the actual subset
    if i == max_pos:
        peaks.append(i) # If the maximum position is where i is, then append that position to the peaks array

peaks = peaks[:-1]
# print(peaks)

# %%
plt.plot(subset)
plt.plot(peaks, subset[peaks], "ro")

# %% [markdown]
# Now we can plot the heart rate using the time between the PPG peaks and the equation above!

# %%
tp = time[peaks] # Create an array of the time at which each peak occurs
delta_t = tp[1:]-tp[:-1] # Find the time between peaks by subtracting t_n-1 from t_n
hr = 60/delta_t # Calculate the heart rate using the equation above
plt.plot(hr)
plt.title("PPG-Derived Heart Rate Using Peak Detection")
plt.xlabel("Time (s)")
plt.ylabel("Heart Rate (bpm)")

# %%
