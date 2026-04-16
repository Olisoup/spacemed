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
#     display_name: Python [conda env:.conda-spacemed26]
#     language: python
#     name: conda-env-.conda-spacemed26-py
# ---

# %% [markdown]
# # Session 5 - Pandas

# %%
import pandas

# %%
station_ids = pandas.read_csv("data/Niederschlag_1981-2010_Stationsliste.txt", encoding="iso-8859-1", engine="python",delimiter=" *; *",index_col="Stations_id") 
# making sure to get the encoding right since it has german characters

# %%
station_ids

# %%
station_ids.columns

# %%
station_ids.info()

# %%
station_ids.head() # First five lines

# %%
station_ids.tail() # Last five lines

# %%
station_ids.columns[-1]

# %%
station_ids.drop(station_ids.columns[-1], axis=1, inplace=True) # Deleting last column, since there is an extra ; causing issues
# Axis 0 = rows and Axis 1 = columns

# %%
station_ids.iloc[2, 0] # Row number 2 (starting at 0) and column 0 -> calling specific indexes

# %%
station_ids.iloc[:5] # Since only putting in one argument automatically goes to one row

# %%
station_ids.iloc[:, 1:3]

# %%
station_ids.loc[3:6, "Stationsname"] # When using names you can use ".loc"

# %%
station_ids.loc[:,"geogr. Breite":"geogr. Laenge"]

# %%
station_ids["Bundesland"]

# %%
station_ids.Bundesland

# %%
station_ids.groupby("Bundesland").count().sort_values("Stationsname", ascending=False) 
#Data sorting by Bundesland, and how it should be sorted + in which order

# %%
# Single column whenever it is Bayern we get TRUE otherwise FALSE
mask = station_ids.Bundesland== "Bayern"

# %%
station_ids[mask]

# %%
# Assigning bayern to the reduced dataframe
bayern = station_ids[mask]

# %%
# Searching in that smaller dataframe
bayern.loc[17]

# %%
Berlinmask = station_ids.Bundesland== "Berlin"

# %%
Berlin = station_ids[Berlinmask]

# %%
station_ids[Berlinmask]

# %%
precipitation = pandas.read_csv("data/Niederschlag_1981-2010.txt", encoding="iso-8859-1", engine="python",delimiter=" *; *",index_col="Stations_id")

# %%
precipitation

# %%
precipitation.drop(precipitation.columns[-1], axis=1, inplace=True)

# %%
precipitation.columns

# %%
precipitation_means = precipitation.loc[:, "Jan.": "Dez."]

# %%
precipitation_means.loc[399]

# %%
precipitation_means.loc[399].plot.bar()

# %%
precipitation_hour = pandas.read_csv("data/produkt_precipitation_399_akt.txt", encoding="iso-8859-1", engine="python",delimiter=" *; *")

# %%
precipitation_hour

# %%
precipitation_hour.head()

# %%
precipitation_hour.MESS_DATUM = pandas.to_datetime(precipitation_hour.MESS_DATUM, format="%Y%m%d%H")

# %%
precipitation_hour["date_time"] = pandas.to_datetime(precipitation_hour.MESS_DATUM, format="%Y%m%d%H")

# %%
precipitation_hour["date_time"]

# %%
precipitation_hour.columns

# %%
precipitation_alexanderplatz = precipitation_hour[["date_time", "NIEDERSCHLAGSHOEHE"]]

# %%
precipitation_alexanderplatz = precipitation_alexanderplatz.rename(columns={"date_time": "date", "NIEDERSCHLAGSHOEHE": "precip"})

# %%
precipitation_alexanderplatz = precipitation_alexanderplatz.set_index("date")

# %%
precipitation_alexanderplatz.precip.plot()

# %%
precipitation_alexanderplatz.plot()

# %%
# Want to go from hourly to monthly so we sum it all up
precipitation_monthly = precipitation_alexanderplatz.resample("ME").sum()

# %%
precipitation_monthly.describe()

# %%
precipitation.loc[399]

# %%
precipitation_monthly.groupby(precipitation_monthly.index.month).describe()

# %%
precipitation_monthly.plot()

# %%
refs = pandas.DataFrame({"precipitation_final": precipitation_means.loc[399].to_list()*12}, index=pandas.date_range("2015-01-01", "2026-12-31", freq="ME"))

# %%
refs

# %%
precipitation_monthly["climate"] = refs

# %%
precipitation_monthly

# %%
precipitation_monthly.plot()

# %%
precipitation_monthly["anomaly"] = precipitation_monthly.precip - precipitation_monthly.climate

# %%
# Overall seems drier than usual 
precipitation_monthly.anomaly.plot()
