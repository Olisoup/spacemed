# ---
# title: "Session 4: Reproducible Documents"
# author: Olivier Soubelet
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
#     display_name: Python [conda env:.conda-spacemed26]
#     language: python
#     name: conda-env-.conda-spacemed26-py
# ---

# %% [markdown]
# # Reproducible Documents & Algorithm Design

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

dataFile = open("data/pulse_data.csv") # Importing the file

# Use a for loop to fill the lists

dataFile.readline() # We don't want to read in the first since it's column headers, so we read through it once to get rid of it in essence

for line in dataFile.readlines(): # Run a for loop through all rows of the file except row 0 
    line = line.split(",") # Split into two lists with the "," delimeter
    time.append(float(line[0])) # Add to the time list
    absorption.append(float(line[1])) # Add to the absorption list

# %%
import numpy # First  things first import your libraries
from matplotlib import pyplot as plt

# %% [markdown]
# ## Data Visualisation

# %%
# Instructing Quarto what to do essentially

#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"


plt.plot(time, absorption) # We create a plot with the lists from earlier
plt.title("Sample Absorption vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Absorption")

# %% [markdown]
# ## Lists & Arrays

# %%
a = numpy.arange(10)+1

# %%
a.shape

# %%
a.dtype

# int64 --> integer require 64 bits of storage

# %%
a.nbytes

# 8 bits in a byte

# %%
b = numpy.array([[1,2,3], [4,5,6]])
b

# %%
b.shape # 2 rows 3 columns

# %%
b.T # Transpose function --> rotates the array 90 degrees (each row becoming a column in essence)

# %%
b.T @ b # @ is dot product, so this is the b-matrix squared

# %%
a # 1 through 10 

# %%
print(numpy.max(a)) # Find MAX
print(numpy.argmax(a)) # Index wher MAX is

# %% [markdown]
# ## Algorithm Design

# %% [markdown]
#  Aim --> Find the heart rate using HR = 60/deltaTpeaks

# %%
# One cycle of PPG

plt.plot(time, absorption, ".")
plt.xlim(time[30], time[250])

# %% [markdown]
# Calculate the heart rate using a basic (w/o automatic functions). For loop that finds the global maximum of each cycle using a window!

# %%
absorption = numpy.array(absorption) # Lists are now numpy arrays
time = numpy.array(time)
# subset = absorption[:1000] # Taking a subset helps during initial testing
subset = absorption
w = 50 # Window for finding global maxmimum
plt.plot(subset)

# %%
peaks1 = [] # New array to store the peaks

# For loop with sliding window of size 2w to find the global maxima for each cycle
for i in range(len(subset)):
    start = max(i-w, 0) # Start the window at i-w unless that is negative, in which case start at 0
    end = min(i+w, len(subset)) # Stop the window at i+w unless > the length of the list, in which case end at the end
    window = subset[start:end] # Get the window
    max_pos = numpy.argmax(window) + start # Position of maximum within the for loop window.
        # "+ start" is needed in order to SHIFT the index of the position back to where it is in the actual subset
    if i == max_pos:
        peaks1.append(i) # If the maximum position is where i is, then append that position to the peaks array

peaks1 = peaks1[:-1]
# print(peaks)

# %%
import pandas # trying the new fancy stuff for this to work

# %%
import scipy

# %%
PPG = pandas.read_csv("data/pulse_data.csv", delimiter="," , encoding='ISO-8859-1', engine= "python")

# %%
PPG

# %%
from scipy.signal import find_peaks
data = absorption
peaks, _ = find_peaks (data, height=2500, distance=1) # setting the minimum height for it to work correctly

# %%
plt.plot(data)
plt.plot(peaks, data[peaks],"ro") # WOOHOOO took me a sec but it worked ! 

# %%
plt.plot(subset)
plt.plot(peaks1, subset[peaks1], "ro")

# %% [markdown]
# Now we can plot the heart rate using the time between the PPG peaks and the equation above! (inital aim aha !)

# %%
tp = time[peaks1] # Create an array of the time at which each peak occurs
delta_t = tp[1:]-tp[:-1] # Find the time between peaks by subtracting t_n-1 from t_n
hr = 60/delta_t # Calculate the heart rate using the equation above
plt.plot(hr)
plt.title("PPG-Derived Heart Rate Using Peak Detection")
plt.xlabel("Time (s)")
plt.ylabel("Heart Rate (bpm)")
