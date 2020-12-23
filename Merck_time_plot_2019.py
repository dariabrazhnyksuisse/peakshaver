# Import necessary packages
from matplotlib import pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt
import dateutil.parser


#datafile CSV
datafile = '/Users/lenovo/kDrive/Common documents/IT/13. Profile Assesments/Git/Merck/peakshaverr/TEST_FILE.csv'
print('loading', datafile)

# import data from CSV file

data = genfromtxt(datafile, delimiter=',')


# select lines to plot
time = data[:,0]
power = data[:,2]

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
