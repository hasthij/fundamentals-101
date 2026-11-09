FIFA RANKINGS: SEABORN PRACTICE

cheat sheet(last lesson)
Trends
sns.lineplot: Change over time.

Relationships
sns.barplot: Quantities by category.
sns.heatmap: Color-coded number patterns.
sns.scatterplot: 2 continuous variables (+1 category by color).
sns.regplot: Scatter + 1 trendline.
sns.lmplot: Scatter + multiple trendlines.
sns.swarmplot: Continuous vs. categorical.

Distributions
sns.histplot: 1 numerical variable distribution.
sns.kdeplot: Smooth 1D/2D density estimate.
sns.jointplot: 2D KDE + 1D side plots combined.

#import these to start
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

lets pandas dates plot properly in matplotlib
pd.plotting.register_matplotlib_converters()


loading the csv to the file
fifa_path = "./data/fifa.csv"

index_col sets Date as the row index, parse_dates turns it into real datetimes
fifa_data = pd.read_csv(fifa_path, index_col="Date", parse_dates=True)

fifa_data.head()


line chart
plt.figure(figsize=(20, 6))

plot single columns to compare two teams (passes the entire dataframe to plot all six)
sns.lineplot(data=fifa_data["ARG"], label="Argentina")
sns.lineplot(data=fifa_data["FRA"], label="France")

plt.title("FIFA Rankings Over Time: Argentina vs France")
plt.ylabel("FIFA rank (lower is better)")
plt.show()

bar chart
plt.figure(figsize=(12, 6))

france_yearly = fifa_data["FRA"]
user .groupby(fifa_data.index.year).mean() because too many rows


sns.barplot(x=france_yearly.index, y=france_yearly.values, color="blue")
plt.title("France: Average FIFA Rank per Year")
plt.xlabel("Year")
plt.ylabel("Average rank (lower is better)")
plt.xticks(rotation=90)
plt.show()

heatmap

plt.figure(figsize=(10, 6))

colour = rank value
sns.heatmap(data=fifa_data)

plt.title("FIFA Rankings by Team and Date")
plt.show()

scatter plot

plt.figure(figsize=(8, 6))

France's rank on x, Argentina's rank on y
sns.scatterplot(x=fifa_data["FRA"], y=fifa_data["ARG"])

plt.title("France vs Argentina Rank")
plt.show()

distribution
bins = number of buckets
kde=True adds the smooth density curve

sns.histplot(fifa_data["ARG"], bins=20, kde=True)
plt.show()

fill=True shades under the curve (newer arg for deprecated shade)
sns.kdeplot(data=fifa_data["ARG"], fill=True, color="r")
plt.show()

2D density of both teams' ranks, 
sns.jointplot(x=fifa_data["ARG"], y=fifa_data["FRA"], kind="kde")
plt.show()

index_col="Date" - makes date the row index
parse_dates=True - turns date strings into real datetimes
figsize=(w, h) - chart size in inches
label= - line name
bins=20 - Number of buckets in the histogram
kde=True - adds the density curve on the histogram
fill=True - shades under a KDE curve (replaced deprecated shade)