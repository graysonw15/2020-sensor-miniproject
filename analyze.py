#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

# Celia's additions:
    
    #take dataframes out of dictionary
    tempdf = data["temperature"]
    occudf = data["occupancy"]
    co2df = data["co2"]
    

    #find the medians and variances
    print("\nTask 2:")
    print("\nThe median temperature of lab1 is:", np.round(tempdf["lab1"].median(),2))
    print("The temperature variance of lab1 is:", np.round(tempdf["lab1"].var(),2))
    print("The median occupancy of lab1 is:", np.round(occudf["lab1"].median(),2))
    print("The occupancy variance of lab1 is:", np.round(occudf["lab1"].var(),2))

    
    #find and plot the pdfs
    plt.figure()
    tempplot = tempdf["lab1"].hist(bins=20)
    plt.title("Lab 1 Temperature Data")
    plt.xlabel("Temperature (℃)")
    plt.figure()
    occuplot = occudf["lab1"].hist(bins=20)
    plt.title("Lab 1 Occupancy Data")
    plt.xlabel("Occupancy (persons)")
    plt.figure()
    co2plot = co2df["lab1"].hist(bins=20)
    plt.title("Lab 1 CO2 Data")
    plt.xlabel("CO2")
    
    for k in data:
    #     # data[k].plot()
        time = data[k].index
    #     # data[k].hist()
    #     # plt.xlabel(k)
    plt.figure()
    plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
    plt.xlabel("Time (seconds)")
    plt.title("Time intervals between data points")

    #mean and variance of time intervals
    timeintervals = np.diff(time.values).astype(np.int64)//1000000000
    print("\nThe mean time interval is ", np.round(np.mean(timeintervals),2))
    print("The time interval variance is ", np.round(np.var(timeintervals),2))
    

    plt.show()

