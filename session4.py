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
#     display_name: Python [conda env:conda_envs-computelab-2025-2]
#     language: python
#     name: conda-env-conda_envs-computelab-2025-2-py
# ---

# %% [markdown]
# *^ Above is metadata we are adding using the raw format*

# %% [markdown]
# *Below we have done some mathematical writing in md. It then goes on to be Latex which is quite useful !*

# %% [markdown]
# # Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# constant mass flow rate $R$ meassured in kg/s
# and _exhaust velocity relative to the rocket
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$ {#eq-rocket-acc}
# Integrating both sides of @eq-rocket-acc from 0
# to $T$ we get

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
# Tell QUARTO how to handle PDF viewing

#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"

pyplot.plot(time,absorption,'m') # Doing it with our actual data, keeping linked because it looks nicer
pyplot.xlabel("Time (s) ")
pyplot.ylabel("Absorption")
pyplot.title("Absorption vs Time")

# %%
