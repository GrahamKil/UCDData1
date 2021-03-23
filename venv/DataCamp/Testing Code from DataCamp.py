# Python Basics
# Example, do not modify!
from xml.dom.minidom import Entity

import inline as inline
import matplotlib

print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)

# Create a variable savings
savings = 100

# Print out savings
print (savings)

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print (result)

# Create a variable desc
desc = "compound interest"
# Create a variable profitable
profitable = True

print(profitable)

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = (savings * growth_multiplier)

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = (desc + desc)

# Print out doubledesc
print(doubledesc)

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

print(pi_float)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = (areas[3] + areas[7])

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas [0:6]

# Use slicing to create upstairs
upstairs = areas [6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage" , 15.45]

print(areas_1)
print(areas_2)

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted= sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r * r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

import pandas as pd

height_in= pd.read_csv("height_in.csv")

# height is available as a regular list
# Import numpy
import numpy as np
import math

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in

# Print np_height_m
print(np_height_m)

# height and weight are available as regular lists

# Import numpy
import numpy as np
import pandas as pd

weight_lb= pd.read_csv("Weight_lb.csv")

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in)

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb)

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m

# Print out bmi
print(bmi)

# height and weight are available as a regular lists

# Import numpy
import numpy as np
import pandas as pd

height_in= pd.read_csv("height_in.csv")

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[: ,1]

# Print out height of 124th player
print(np_baseball[123, 0])

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
# print(np_baseball + updated)
# made this a note so that script will run for the rest
# NameError: name 'updated' is not defined

# Create numpy array: conversion
conversion = 0.0254, 0.453592, 1

# Print out product of np_baseball and conversion
# print(np_baseball * conversion)
# made this a note so that script will run for the rest
# ValueError: operands could not be broadcast together with shapes (194,2) (3,)

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

# Basic plot with Matplotlib

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Print the last item from year and pop
print(year[-1]), print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#import data
df = pd.read_csv('life-expectancy-vs-gdp-per-capita.csv')
df=df.dropna(how='any')

# Print the last item of gdp_cap and life_exp
print('Real GDP per capita in 2011US$' [-1]), print('Life expectancy' [-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.scatter('Real GDP per capita in 2011US$', 'Life expectancy')

# Display the plot
plt.show()

# Change the line plot below to a scatter plot
plt.scatter('Real GDP per capita in 2011US$', 'Life expectancy')

import matplotlib.pyplot as plt

# Put the x-axis on a logarithmic scale
# plt.xscale('log')
# making a comment as the above gives error

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter('Total population', 'Life expectancy')

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Create histogram of life_exp data
plt.hist('Life expectancy')

# Display histogram
plt.show()

# Build histogram with 5 bins
plt.hist('Life expectancy', 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist('Life expectancy', 20)

# Show and clean up again
plt.show()
plt.clf()

# Histogram of life_exp, 15 bins
plt.hist('Life expectancy', 15)

# Show and clear plot
plt.show()
plt.clf()

life_exp1950 = [1950,7752000, 27.638, 2392]

# Histogram of life_exp1950, 15 bins
plt.hist('life_exp1950', 15)

# Show and clear plot again
plt.show()
plt.clf()

import matplotlib.pyplot as plt

df = pd.read_csv('life-expectancy-vs-gdp-per-capita.csv')
df=df.dropna(how='any')

# Basic scatter plot, log scale
plt.scatter('Real GDP per capita in 2011US$', 'Life expectancy')
# plt.xscale('log')
# made this a comment due to error
# Data has no positive values, and therefore cannot be log-scaled.
#   plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# After customizing, display the plot
plt.show()

# Scatter plot
plt.scatter('Real GDP per capita in 2011US$', 'Life expectancy')

# Previous customizations
# plt.xscale('log')
# made this a comment due to error
# Data has no positive values, and therefore cannot be log-scaled.
#   plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# After customizing, display the plot
plt.show()

# Import numpy as np
import numpy as np

Total_population = 'np_pop'

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop *2

# Update: set s argument to np_pop
# plt.scatter('Real GDP per capita in 2011US$', 'Life expectancy', s= np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'}

col = dict

# Specify c and alpha inside plt.scatter()
# plt.scatter(x = 'Real GDP per capita in 2011US$' , y = 'Life expectancy', s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

# Scatter plot
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'population': 59.83, 'capital': 'rome'}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
dict = {
        'country':['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
        'drives_right':[True, False, False, False, True, True, True],
        'cars_per_cap':[809, 731, 588, 18, 200, 70, 45]}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(dict)

# Print cars
print(cars)

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
# cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
# cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:4])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

# Comparison of booleans
True == False

# Comparison of integers
-5*15 != 75

# Comparison of strings
"pyscript" == "PyScript"

# Compare a boolean with an integer
True == 1

# Comparison of integers
x = -3 * 6
x >= -10

# Comparison of strings
y = "test"
"test" <= y

# Comparison of booleans
True > False

import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen > 14 or my_kitchen < 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen *2 > your_kitchen *3)

import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5,
                    my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11,
                     your_house < 11))

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
else:
    print("looking around elsewhere.")

# if-else construct for area
if area > 15:
    print("big place!")
else:
    print("pretty small.")

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]


# Print sel
print(sel)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)

# Initialize offset
offset = 8

# Code the while loop
while offset  != 0 :
    print("correcting...")
    offset = offset -1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1

    print(offset)

fam = [1.73, 1.68, 1.71, 1.89]
for height in fam :
    print(height)

for index, height in enumerate(fam) :
    print("index" + str(index) + ": " + str(height))

for c in 'family' :
    print(c.capitalize())

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for areas in areas :
    print(areas)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, a in enumerate(areas):
    print("room" + str(index+1) + " : " + str(a))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room, area in house:
    print("the " + str(room) + " is " + str(area) + " sqm")

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print('the capital of', key + " is " + str(value))

# Import numpy as np
import numpy as np

np_height = [74, 74, 72, ..., 75, 75, 73]

# For loop over np_height
for x in np_height:
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row["cars_per_cap"]))

# Import cars data
import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))

# Numpy is imported, seed is set
np.random.seed(123)
# Starting step
step = 50

# Roll the dice
dice = (np.random.randint(1, 7))

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif  dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice), print(step)

# Numpy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

     # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for random_walk in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()