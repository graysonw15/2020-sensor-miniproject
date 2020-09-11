# This file incorporates the design portion of the miniproject.
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
from analyze import load_data

# Calling data-read function from analyze.py
if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)


# Task 3: Design (Grayson)

    # Take dataframes out of dictionary
    tempdf = data["temperature"]
    occudf = data["occupancy"]
    co2df = data["co2"]
    print("\nTask 3: Design")
    print("Temperature Anomaly Detection:")

    # Plots untouched temperature data
    tempplot = tempdf.plot()
    plt.title("Unedited Temperature Plot")
    plt.xlabel("Time")
    plt.ylabel(u'Temperature (℃)')
    plt.ylim([0, 2000])

    # Drops temperatures that are deemed impossible to occur
    dropdf = tempdf[(tempdf[:] > -31.5) & (tempdf[:] < 65.5)]
    dropdf = dropdf.dropna(axis=0, how='all')
    outlier = tempdf[(tempdf[:] < -31.5) | (tempdf[:] > 65.5)]
    outlier = outlier.dropna(axis=0, how='all')

    # Plots the Outlier-filtered plot and pdf
    outplot = dropdf.plot()
    plt.title("Outlier-Filtered Temperature Plot")
    plt.xlabel("Time")
    plt.ylabel(u'Temperature (℃)')
    outpdf = dropdf.plot.kde()
    plt.title("Outlier-Filtered Temperature PDF")
    plt.xlabel(u'Temperature (℃)')
    plt.xlim([10, 40])

    # Defines the mean and standard deviation of data 
    print("\nDropped outlier temperature points, next check gaussian-filtering:")
    print("The mean temperature is:\n", dropdf.mean())
    print("The temperature standard deviation is:\n", dropdf.std())

    # Filters out the temperature data outside of 2 std. deviations
    filterdf = dropdf[np.abs(dropdf-dropdf.mean()) <= (2*dropdf.std())]
    filterdf = filterdf.dropna(axis=0, how='all')
    gaussf = dropdf[np.abs(dropdf-dropdf.mean()) > (2*dropdf.std())]
    gaussf = gaussf.dropna(axis=0, how='all')

    # Plots the gaussian-filtered data
    filterplot = filterdf.plot()
    plt.title("Gaussian-Filtered Temperature Plot")
    plt.xlabel("Time")
    plt.ylabel(u'Temperature (℃)')   

    # Saves Outliers and Filtered Terms into a .csv file
    anamolies = pandas.concat([outlier,gaussf])
    anamolies.to_csv('anamolies_log.csv')

    
    # Prints relative stats (ie. upper/lower bounds, mean)
    print("\nFiltered temperatures and created anomolies_log in directory.")
    print("The temperature bounds for lab1 is: [", np.round(np.nanmin(filterdf["lab1"]),2), ",", 
        np.round(np.nanmax(filterdf["lab1"]),2), "] (℃)")
    print("The temperature bounds for office is: [", np.round(np.nanmin(filterdf["office"]),2), ",", 
        np.round(np.nanmax(filterdf["office"]),2), "] (℃)")
    print("The temperature bounds for class1 is: [", np.round(np.nanmin(filterdf["class1"]),2), ",", 
        np.round(np.nanmax(filterdf["class1"]),2), "] (℃)\n")
    
    plt.show()

