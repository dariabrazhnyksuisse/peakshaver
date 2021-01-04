# Import necessary packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.font_manager import FontProperties

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sns.set(font_scale=1, style="whitegrid")


# The path to file
file_path = ('TEST_FILE.csv')

#date format
date_format = '%Y-%d-%m %H:%M^%S'

# To import the dates as a datetime object with parse_dates
# index_col to set the index of the dataframe to the datetime values
# Read csv file and Import file into pandas dataframe
data_2019 = pd.read_csv(file_path,
                            parse_dates=['date'], index_col=['date'])

# Display the entire value
print(data_2019.to_string())

# Display first rows
data_2019.head()

# View dataframe info
data_2019.info()

print("Index Values: ")
print(data_2019.index.values)
print("----------------------------------")
# Subset data to Jan-Feb 2019
power_jan_feb_2019 = data_2019['2019-01-01':'2019-02-28']
power_jan_feb_2019.head()
print("----------------------------------")

# View column data types
data_2019.dtypes

#font common
font = FontProperties()
font.set_name('Calibri')


# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10), tight_layout=True)

#formatter for dates
#formatter = power_jan_feb_2019.DateFormatter('%d-%m')

# Add x-axis and y-axis
ax.plot(power_jan_feb_2019.index.values,
        power_jan_feb_2019['power'],
        color='DeepSkyBlue', label='Nice Blue Line')


#try
plt.grid(True)
plt.legend(loc='upper right',prop={'size':12})

plt.axis(ymin=120, ymax=800)

# Set title and labels for axes
ax.set_xlabel("Date", fontproperties=font)
ax.set_ylabel("Power [kW]", fontproperties=font)
ax.set_title("Merck Jan-Feb 2019", fontsize='large', fontweight='bold', fontproperties=font)

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=50)

plt.show()
