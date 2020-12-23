# Import necessary packages
from matplotlib import pyplot as plt
import numpy as np
from numpy import genfromtxt
from datetime import datetime
import pandas as pd


dateparse = lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M:%S')

#datafile CSV
datafile = '/Users/lenovo/kDrive/Common documents/IT/13. Profile Assesments/Git/Merck/peakshaver/TEST_FILE.csv'
print('loading', datafile)

# import data from CSV file

df = pd.read_csv(datafile, parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)


# select lines to plot
time = df[:,0]
power = df[:,2]

print("print time")
print(time)
print("print power")
print(power)


print("------------------------ Start plot --------------------")
plt.plot(time, power)
plt.title("GRZ Technologies SA, Stationary Fuel Cell Project Merck \n Approximate Yearly Usage")
plt.xlabel('01-02/2019')
plt.ylabel('Power [kW]')
plt.show()
