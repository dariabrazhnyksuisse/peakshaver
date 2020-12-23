# Import necessary packages
from matplotlib import pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt


anyString = '47586[kW]'
print("Result String:")
print(anyString[:-4])


anyDate = '9 Jun 2019 02:09:00'


#dateTime convertor
def date_convert(d_bytes):
    s = d_bytes.decode('utf-8')
    return np.datetime64(dt.datetime.strptime(s, '%d %b %Y %H:%M:%S'))

#strInteger convertor
def string_convert(s):
#we need to substring last 4 signs "[kW]"
    s[:-4]
    return int(s)

#file path
file_path = '/Users/lenovo/kDrive/Common documents/IT/13. Profile Assesments/Merck/2020-58-22_Merck_Profile.csv'


# import data from CSV file
data = genfromtxt(file_path, converters={0: date_convert, 1: string_convert}, delimiter=',')
# select lines to plot
time = data[:,0]
power = data[:,1]


# Subset data to January-February 2019
# time_jan_feb_2019 = time['15 Jan 2019 00:00:00':'15 Feb 2019 23:59:59']

#test git commit

print("------------------------ Start plot --------------------")
#plt.plot(time_jan_feb_2019, power)
plt.plot(time, power)
plt.title("GRZ Technologies SA, Stationary Fuel Cell Project Merck \n Approximate Yearly Usage")
plt.xlabel('01-02/2019')
plt.ylabel('Power [kW]')
plt.show()
