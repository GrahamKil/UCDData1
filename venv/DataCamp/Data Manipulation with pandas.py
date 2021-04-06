#### Transforming Data

# INSPECTING A DATAFRAME

.head() returns the first few rows
    (the “head” of the DataFrame).

.info() shows information on each of the columns,
    such as the data type and number of missing values.

.shape returns the number of rows and columns of
    the DataFrame.

.describe() calculates a few summary statistics for
    each column.

#1
# Print the head of the homelessness data
print(homelessness.head())

#2
# Print information about homelessness
print(homelessness.info())

#3
# Print the shape of homelessness
print(homelessness.shape)

#4
# Print a description of homelessness
print(homelessness.describe())






# PART OF A DATAFRAME

.values : A two-dimensional NumPy array of values.
.columns : An index of columns: the column names.
.index : An index for the rows: either row numbers or row names.


# Import pandas using the alias pd
import pandas as pd

#1
# Print the values of homelessness
print(homelessness.values)

#2
# Print the column index of homelessness
print(homelessness.columns)

#3
# Print the row index of homelessness
print(homelessness.index)





#SORTING AND SUBSETTING

Sort on …	Syntax
one column	df.sort_values("breed")
multiple columns	df.sort_values(["breed", "weight_kg"])
By combining .sort_values() with .head(), you can answer questions in the form, "What are the top cases where…?".

homelessness is available and pandas is loaded as pd.

#1
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

#2
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members',ascending=False)

# Print the top few rows
print(homelessness_fam.head())

#3
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'], ascending = [True, False])

# Print the top few rows
print(homelessness_reg_fam.head())







# SETTING COLUMNS

Subsetting columns
When working with data, you may not need all of the
variables in your dataset. Square brackets ([]) can be
used to select only the columns that matter to you in an
order that makes sense to you. To select only "col_a" of
the DataFrame df, use

df["col_a"]
To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]
homelessness is available and pandas is loaded as pd.


#1
# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())

#2
# Select the state and family_members columns
state_fam = homelessness[['state','family_members']]

# Print the head of the result
print(state_fam.head())

#3
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

# Print the head of the result
print(ind_state.head())






# SUBSETTING ROWS

Subsetting rows
A large part of data science is about finding
which bits of your dataset are interesting. One of the
simplest techniques for this is to find a subset of
rows that match some criteria. This is sometimes known
as filtering rows or selecting rows.

There are many ways to subset a DataFrame, perhaps
the most common is to use relational operators
to return True or False for each row, then pass that
inside square brackets.

dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
You can filter for multiple conditions at once by using the "bitwise and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
homelessness is available and pandas is loaded as pd.


#1
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]

# See the result
print(ind_gt_10k)

#2
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region']=="Mountain"]

# See the result
print(mountain_reg)

#3
# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) & (homelessness['region']=="Pacific")]

# See the result
print(fam_lt_1k_pac)








# SUBSETTING ROWS BY CATEGORICAL VARIABLES

Subsetting rows by categorical variables
Subsetting data based on a categorical variable often
involves using the "or" operator (|) to select rows from
multiple categories. This can get tedious when you
want all states in one of three different regions, for
example. Instead, use the .isin() method, which will
allow you to tackle this problem by writing one
condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
homelessness is available and pandas is loaded as pd.


#1
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region']=="South Atlantic") | (homelessness['region']=="Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

#2
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)








# NEW COLUMNS

Adding new columns
You aren't stuck with just the data you are given.
Instead, you can add new columns to a DataFrame.
This has many names, such as transforming, mutating,
and feature engineering.

You can create new columns from scratch, but it is
also common to derive them from other columns,
for example, by adding columns together or by
changing their units.

homelessness is available and pandas is loaded as pd.

#1
# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)





### COMBO-ATTACK!

You've seen the four most common types of '
data manipulation: sorting rows, subsetting
columns, subsetting rows, and adding new columns.
In a real-life data analysis, you can mix and match
these four manipulations to answer a multitude of questions.

In this exercise, you'll answer the question, '
"Which state has the highest number of homeless
"individuals per 10,000 people in the state?"
Combine your new pandas skills to find out.


#1
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k']>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)












# CHAPTER 2 - Aggregating Data
# SUMMARY STATISTICS

Mean and median
Summary statistics are exactly what they sound
like - they summarize many numbers in one statistic.
For example, mean, median, minimum, maximum, and
standard deviation are summary statistics.
Calculating summary statistics allows you to get a
better sense of your data, even if there's a lot of it.

sales is available and pandas is loaded as pd.


#1
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())


# SUMMRIZING DATES

Summary statistics can also be calculated on date
columns that have values with the data type datetime64.
Some summary statistics — like mean —
don't make a ton of sense on dates, but others are super helpful, ' \
for example, minimum and maximum, which allow you to see what time range your data covers.

sales is available and pandas is loaded as pd.


#1
# Print the maximum of the date column
print(sales['date'].max())
<script.py> output:
> 2012-10-26 00:00:00

# Print the minimum of the date column
print(sales['date'].min())
<script.py> output:
> 2010-02-05 00:00:00







# Efficient summaries

While pandas and NumPy have tons of functions,
sometimes, you may need a different function to summarize your data.

The .agg() method allows you to apply your own custom
functions to a DataFrame, as well as apply functions to more
than one column of a DataFrame at once, making your
aggregations super-efficient. For example,

df['column'].agg(function)
In the custom function for this exercise, "IQR" is short for
inter-quartile range, which is the 75th percentile minus
the 25th percentile. It's an alternative to standard deviation'
 that is helpful if your data contains outliers.

sales is available and pandas is loaded as pd.


#1
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

#2
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
<script.py> output:
> temperature_c           16.583
  fuel_price_usd_per_l     0.073
  unemployment             0.565
  dtype: float64

#3
# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
<script.py> output:
>         temperature_c  fuel_price_usd_per_l  unemployment
iqr            16.583                 0.073         0.565
median         16.967                 0.743         8.099













# CUMULATIVE STATISTICS

.cummax(),.cummin(), .cumprod()

Cumulative statistics
Cumulative statistics can also be helpful in
tracking summary statistics over time. In this
exercise, you'll calculate the cumulative sum and cumulative
max of a department's weekly sales, which will allow you to
identify what the total sales were so far as well as what
the highest weekly sales were so far.

A DataFrame called sales_1_1 has been created for you,
which contains the sales data for department 1 of store 1. pandas
is loaded as pd.


#1
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date', ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])









##### COUNTING

# Dropping duplicates

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates('date')

# Print date col of holiday_dates
print(holiday_dates['date'])





# Counting categorical variables

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)









# Grouped summary statistics

.groupby()

# What percent of sales occurred at each store type?
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / (sales_A+sales_B+sales_C)
print(sales_propn_by_type)
> [0.9097747 0.0902253 0.       ]






# Calculations with .groupby()
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type/sum(sales.weekly_sales)
print(sales_propn_by_type)
> type
  A    0.91
  B    0.09
  Name: weekly_sales, dtype: float64

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type",'is_holiday'])["weekly_sales"].sum()
print(sales_by_type_is_holiday)
<script.py> output:
> type  is_holiday
  A     False         2.337e+08
        True          2.360e+04
  B     False         2.318e+07
        True          1.621e+03
  Name: weekly_sales, dtype: float64








# Multiple grouped summaries
# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)










# Pivot tables
# The .pivot_table() method is just an alternative to .groupby().

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)
<script.py> output:
>       weekly_sales
  type
  A        23674.667
  B        25696.678

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index= 'type', aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)
<script.py> output:
>              mean       median
       weekly_sales weekly_sales
  type
  A       23674.667     11943.92
  B       25696.678     13336.08

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index= 'type', columns='is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
<script.py> output:
> is_holiday      False    True
  type
  A           23768.584  590.045
  B           25751.981  810.705







# Fill in missing values and sum values with pivot tables

# The .pivot_table() method has several useful arguments, including fill_value and margins.
#
# fill_value replaces missing values with a real value (known as imputation).
# margins is a shortcut for when you pivoted by two variables,
# but also wanted to pivot by each of those variables
# separately: it gives the row and column totals of the pivot table
# contents.

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))










### Slicing and indexing
# EXPLICIT INDEXES
# Setting & removing indexes

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))











# Slicing and subsetting with .loc and .iloc
# Make a list of cities to subset on
cities = ['Moscow', 'Saint Petersburg']

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])









# Setting multi-level indexes
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"),("Pakistan","Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])










# Sorting by index values
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country','city'], ascending=[True, False]))








# Slicing and subsetting with .loc and .iloc
# Slicing index values

# Compared to slicing lists, there are a few things to remember.

# You can only slice an index if the index is sorted (using .sort_index()).
# To slice at the outer level, first and last can be strings.
# To slice at inner levels, first and last should be tuples.
# If you pass a single slice to .loc[], it will slice the rows.


# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])
<script.py> output:
                               date  avg_temp_c
country  city
Pakistan Faisalabad       2000-01-01      12.792
         Faisalabad       2000-02-01      14.339
         Faisalabad       2000-03-01      20.309
         Faisalabad       2000-04-01      29.072
         Faisalabad       2000-05-01      34.845

Russia   Saint Petersburg 2013-05-01      12.355
         Saint Petersburg 2013-06-01      17.185
         Saint Petersburg 2013-07-01      17.234
         Saint Petersburg 2013-08-01      17.153
         Saint Petersburg 2013-09-01         NaN


# Try to subset rows from Lahore to Moscow (This will return nonsense.)
print(temperatures_srt.loc['Lahore':'Moscow'])
<script.py> output:
                         date  avg_temp_c
country city
Mexico  Mexico     2000-01-01      12.694
        Mexico     2000-02-01      14.677
        Mexico     2000-03-01      17.376
        Mexico     2000-04-01      18.294
        Mexico     2000-05-01      18.562
...                       ...         ...
Morocco Casablanca 2013-05-01      19.217
        Casablanca 2013-06-01      23.649
        Casablanca 2013-07-01      27.488
        Casablanca 2013-08-01      27.952
        Casablanca 2013-09-01         NaN

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan','Lahore'):('Russia', 'Moscow')])
<script.py> output:
                    date  avg_temp_c
country  city
Pakistan Lahore 2000-01-01      12.792
         Lahore 2000-02-01      14.339
         Lahore 2000-03-01      20.309
         Lahore 2000-04-01      29.072
         Lahore 2000-05-01      34.845
...                    ...         ...
Russia   Moscow 2013-05-01      16.152
         Moscow 2013-06-01      18.718
         Moscow 2013-07-01      18.136
         Moscow 2013-08-01      17.485
         Moscow 2013-09-01         NaN

[660 rows x 2 columns]










# Slicing in both directions

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])











# Slicing time series
# Add the date column to the index, then use .loc[] to perform
# the subsetting. The important thing to remember is to keep
# your dates in ISO 8601 format, that is, yyyy-mm-dd.

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])










# Subsetting by row/column number
# This is done using .iloc[], and like .loc[], it can take
# two arguments to let you subset by rows and columns.

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,2])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5,:])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:5,2:4])








### Working with pivot tables
## Pivot temperature by city and year
# You can access the components of a date
# (year, month and day) using code of the
# form dataframe["column"].dt.component.
# For example, the month component is
# dataframe["column"].dt.month, and the year component
# is dataframe["column"].dt.year.

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country','city'], columns='year')

# See the result
print(temp_by_country_city_vs_year)
<script.py> output:
year                              2000    2001    2002    2003    2004  ...    2009    2010    2011    2012    2013
country       city                                                      ...
Afghanistan   Kabul             15.823  15.848  15.715  15.133  16.128  ...  15.093  15.676  15.812  14.510  16.206
Angola        Luanda            24.410  24.427  24.791  24.867  24.216  ...  24.325  24.440  24.151  24.240  24.554
Australia     Melbourne         14.320  14.180  14.076  13.986  13.742  ...  14.647  14.232  14.191  14.269  14.742
              Sydney            17.567  17.855  17.734  17.592  17.870  ...  18.176  17.999  17.713  17.474  18.090
Bangladesh    Dhaka             25.905  25.931  26.095  25.927  26.136  ...  26.536  26.648  25.803  26.284  26.587
...                                ...     ...     ...     ...     ...  ...     ...     ...     ...     ...     ...
United States Chicago           11.090  11.703  11.532  10.482  10.943  ...  10.298  11.816  11.214  12.821  11.587
              Los Angeles       16.643  16.466  16.430  16.945  16.553  ...  16.677  15.887  15.875  17.090  18.121
              New York           9.969  10.931  11.252   9.836  10.389  ...  10.142  11.358  11.272  11.972  12.164
Vietnam       Ho Chi Minh City  27.589  27.832  28.065  27.828  27.687  ...  27.853  28.282  27.675  28.249  28.455
Zimbabwe      Harare            20.284  20.861  21.079  20.889  20.308  ...  20.524  21.166  20.782  20.523  19.756

[100 rows x 14 columns]









## Subsetting pivot tables
# A pivot table is just a DataFrame with sorted indexes.
# the .loc[] + slicing combination is often helpful.
# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']
<script.py> output:
year                    2005    2006    2007    2008    2009    2010
country  city
Egypt    Cairo        22.006  22.050  22.361  22.644  22.625  23.718
         Gizeh        22.006  22.050  22.361  22.644  22.625  23.718
Ethiopia Addis Abeba  18.313  18.427  18.143  18.165  18.765  18.298
France   Paris        11.553  11.788  11.751  11.278  11.464  10.410
Germany  Berlin        9.919  10.545  10.883  10.658  10.062   8.607
India    Ahmadabad    26.828  27.283  27.511  27.049  28.096  28.018
         Bangalore    25.476  25.418  25.464  25.353  25.726  25.705
         Bombay       27.036  27.381  27.635  27.178  27.845  27.765
         Calcutta     26.729  26.986  26.585  26.522  27.153  27.289
         Delhi        25.716  26.366  26.146  25.675  26.554  26.520











## Calculating on a pivot table
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year==mean_temp_by_year.max()])
<script.py> output:
> year
  2013    20.312
  dtype: float64

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city==mean_temp_by_city.min()])
<script.py> output:
> country  city
  China    Harbin    4.877
  dtype: float64














### Creating and Visualizing DataFrames
## Visualizing your data
# Which avocado size is most popular?

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

<script.py> output:
             date          type  year  avg_price   size    nb_sold
    0  2015-12-27  conventional  2015       0.95  small  9.627e+06
    1  2015-12-20  conventional  2015       0.98  small  8.710e+06
    2  2015-12-13  conventional  2015       0.93  small  9.855e+06
    3  2015-12-06  conventional  2015       0.89  small  9.405e+06
    4  2015-11-29  conventional  2015       0.99  small  8.095e+06

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
plt.show()








## Changes in sales over time

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')

# Show the plot
plt.show()








## Avocado supply and demand
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter',title="Number of avocados sold vs. average price")

# Show the plot
plt.show()











## Price of conventional vs. organic avocados

# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist(bins=20, alpha=0.5)

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins=20, alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()










### Missing values
## Finding missing values
.isna(), .any()

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
print(avocados_2016.isna())

# Print a summary that shows whether any value in each column is missing or not.
print(avocados_2016.isna().any())

date False
avg_price False
total_sold False
small_sold True
large_sold True
xl_sold True
total_bags_sold False
small_bags_sold False
large_bags_sold False
xl_bags_sold False
dtype: bool

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()











## Removing missing values
.dropna()

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
> date               False
  avg_price          False
  total_sold         False
  small_sold         False
  large_sold         False
  xl_sold            False
  total_bags_sold    False
  small_bags_sold    False
  large_bags_sold    False
  xl_bags_sold       False
  dtype: bool








## Replacing missing values
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()











### Creating DataFrames

## List of dictionaries

# Create a list of dictionaries with new data
avocados_list = [
    {'date': "2019-11-03", 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
>          date  small_sold  large_sold

<script.py> output:
             date  small_sold  large_sold
    0  2019-11-03    10376832     7835071
    1  2019-11-10    10717154     8561348










## Dictionary of lists

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)
>          date  small_sold  large_sold
  0  2019-11-17    10859987     7674135
  1  2019-12-01     9291631     6238096













### Reading and writing CSVs
## CSV to DataFrame

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())
>              airline  year  nb_bumped  total_passengers
  0    DELTA AIR LINES  2017        679          99796155
  1     VIRGIN AMERICA  2017        165           6090029
  2    JETBLUE AIRWAYS  2017       1475          27255038
  3    UNITED AIRLINES  2017       2067          70030765
  4  HAWAIIAN AIRLINES  2017         92           8422734

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)

> airline
ALASKA AIRLINES           1392          36543121          0.381
AMERICAN AIRLINES        11115         197365225          0.563
DELTA AIR LINES           1591         197033215          0.081
EXPRESSJET AIRLINES       3326          27858678          1.194
FRONTIER AIRLINES         1228          22954995          0.535
HAWAIIAN AIRLINES          122          16577572          0.074
JETBLUE AIRWAYS           3615          53245866          0.679
SKYWEST AIRLINES          3094          47091737          0.657
SOUTHWEST AIRLINES       18585         228142036          0.815
SPIRIT AIRLINES           2920          32304571          0.904
UNITED AIRLINES           4941         134468897          0.367
VIRGIN AMERICA             242          12017967













## DataFrame to CSV
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

>                     nb_bumped  total_passengers  bumps_per_10k
airline
EXPRESSJET AIRLINES       3326          27858678          1.194
SPIRIT AIRLINES           2920          32304571          0.904
SOUTHWEST AIRLINES       18585         228142036          0.815
JETBLUE AIRWAYS           3615          53245866          0.679
SKYWEST AIRLINES          3094          47091737          0.657
AMERICAN AIRLINES        11115         197365225          0.563
FRONTIER AIRLINES         1228          22954995          0.535
ALASKA AIRLINES           1392          36543121          0.381
UNITED AIRLINES           4941         134468897          0.367
VIRGIN AMERICA             242          12017967          0.201
DELTA AIR LINES           1591         197033215          0.081
HAWAIIAN AIRLINES          122          16577572          0.074

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")