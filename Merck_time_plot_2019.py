# Import necessary packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sns.set(font_scale=1.5, style="whitegrid")



# Define relative path to file
file_path = ('TEST_FILE.csv')

# Import file into pandas dataframe
data_2019 = pd.read_csv(file_path)


# Display first rows
data_2019.head()

# View dataframe info
data_2019.info()

# View column data types
data_2019.dtypes

# Check data type of first value in date column
type(data_2019['date'][0])

# Check data type of second value in time column
type(data_2019['time'][1])

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))


# Check data type of third value in power column
type(data_2019['power'][2])

# Add x-axis and y-axis
ax.plot(data_2019['date'],
        data_2019['power'],
        color='DeepSkyBlue')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Power [kW]",
       title="Merck 2019")

plt.show()
