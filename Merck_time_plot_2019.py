# Import necessary packages
from matplotlib import pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt
import dateutil.parser


#datafile CSV
datafile = '/Users/lenovo/kDrive/Common documents/IT/13. Profile Assesments/Git/Merck/peakshaverr/2020-58-22_Merck_Profile.csv'
print('loading', datafile)

# import data from CSV file

data = np.genfromtxt(datafile, delimiter=';',  dtype=None, converters={0: dateutil.parser.parse})


# select lines to plot
time = data[:,0]
power = data[:,1]

print("prin time")
print(time)
print("prin power")
print(power)


print("------------------------ Start plot --------------------")
plt.plot(time, power)
plt.title("GRZ Technologies SA, Stationary Fuel Cell Project Merck \n Approximate Yearly Usage")
plt.xlabel('01-02/2019')
plt.ylabel('Power [kW]')
plt.show()
