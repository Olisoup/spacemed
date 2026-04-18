# 2026-03-12 Olivier's Session 5 Reflection

## Description of the session

Today was all about virtual environments! We learned a few tips on how to handle our own environments and the different options that exist. In our cas we are
working with **conda.**

From there we started working with pandas, I was super impressed with the implications of this package. It is so convenient for handlling data. Especially in our case
in physiology research, its ability to handle time series and heterogeneous columns is great :) (and missing data obviously aha)

We looked at data from the "DWD open data", basically weather data from Berlin, and we were seeking to compare the current precipitation in Alexanderplatz, to the past
30 year average precipiation in Germany, and compute the anomaly.

We essentially loaded the data from these datasets, searched for our location of interest, manipulated the dataframes to fit our data comparison (monthly means) and plotting 
them against each other, ultimately finding the delta to quantify the difference, showing that overall it has been drier than the last 30 years (probably due to climate
change).

## Written Feedback & Reflection on the session

1. **The structure of the session**: Once again great structure, loading everything in and breaking it down into digestible pieces of information.
2. **The pace of the session**: The pace was comfortable, I quite enjoyed it !
3. **Theory vs practical**: Similarly to session 4, going through a full example made a lot of sense, I really enjoyed it.
4. **Difficulty level**: Slightly easier in my opinion than last week's session. The possibilites with pandas are wonderful ! So many options for data analysis and it simplifies so many things.


## Key Learning Points

1. Conda & Pandas
2. Manipulating data with Pandas with a practical example

## Future To-Do

- [ ] Look more into Pandas, try to use it for Spacemed projects
- [ ] Check the book that was mentioned, maybe sign up for a Python course, with mini projects
