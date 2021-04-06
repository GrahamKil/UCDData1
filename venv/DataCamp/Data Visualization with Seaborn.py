### Introduction to Seaborn

## Making a scatter plot with lists

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()







## Making a count plot with a list

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()










## "Tidy" vs. "untidy" data

# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df= pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())
<script.py> output:
 Unnamed: 0               How old are you?
0     Marion                             12
1      Elroy                             16
2        NaN  What is your favorite animal?
3     Marion                            dog
4      Elroy                            cat












## Making a count plot with a DataFrame

# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()