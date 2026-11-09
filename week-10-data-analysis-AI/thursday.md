Pandas Library

importing
import pandas as pd

a dataframe is a table
implementing structure shown in example
pd.DataFrame({'Bob': [50, 21], 'Sue': [131, 2]})

pd.DataFrame({'Bob': [50, 21], 'Sue': [131, 2]})

the key are the columns
the values are the rows to the respect key coloumn
Visually this is 

|    |Bob|Sue|
|0   |50 |131|
|1   |21 |2  |

to control the left hand naming rows(indexes)
pass index with a list 

example:

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

|	     |Bob          |Sue
|Product A|I liked it.  |Pretty good.
|Product B|It was awful.|Bland.


Series is one sequence or coloumn of data
example 
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

gives 

|2015 Sales|30
|2016 Sales|35
|2017 Sales|40
|Name: Product A, dtype: int64


reading data files(csv)

extract = pd.read_csv(<path to csv file>)

extract.shape() would give you the column and row count

extract.head() would give you the first five rows of data (including the column and row names)

pandas sometimes doesnt pick up the indexing coloumn naturally, to bind a existin coloumn as a indexing coloumn, use  ,index_col=0
a full line of code would look like this

extract = pd.read_csv(<path to csv file>,index_col=0)

to_csv(<path to csv file>)

,index= Fales this controls if pandas saves the indexs


Selecting
Can index like normal dictionary
reviews.country where .<coloumn name>

but this is safe as it can handle specialized names like country region
reviews['country region'][0]

iloc and loc

iloc is interger based(using integers)
example
reviews.iloc[0]
getting a coloumn would be 
reviews.iloc[:,0]
: means everything

just like normal splicing
[-5:]
would give the last 5 rows(rows first)

using a [[1,2],0] would first two rows of the first coloumns


loc is name based
reviews.loc["country] would return the coloumn, if yu add [0] it would return the first row of country coloumn  
like this 
reviews.loc[:99,["country","variety"]]


reviews.loc[:,['taster_name', 'taster_twitter_handle', 'points']]
can have conditions like reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

Note: Use :, when you neeed to pull everything else specify

remember both of these functions pull row first coloumn while native py pulls it the opposite, matters alot of iloc


assigning is 
reviews['critic'][<yu can have positions here>] = 'everyone' or range(len(reviews), 0, -1)

use this to set an index
reviews.set_index("title")


Summary Functions

review.points.describe()
describe()
gives a more descriptive output on the data coloumn

mean()

remeaning the points to equal to 0 (this shows a weight, negative means less that mean and vice versa)
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

this function takes in a row, adjusts only the point to the new points and changes the value to the weight
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

groupby analysis
reviews.groupby("point").points.count()

can pass in multiple different function like .apply and min()

another examples

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

.str.contains("<string>").sum can be used to count how many rows have the string in them

where .idxmax is returning the index value of pipe
and multiple coloumns as a list , reviews.groupby(['country', 'province'])
last() to get the last itewm

to convert multi_index back to regular index use reset_index()

Sorting

.sort_values(by=["country","province"], ascending=False)

.sort_index()


Dtypes, Datatypes in a Series or DataFrame
reviews.price.dtype

dtypes is used to get properties

Missing data
notnull() or null()

replacing Missing Data("Nan's)

reviews.country.fillna("Unknown")

or for updating use .replace()
reviews.name.replace("Unknown","NotFound")

renaming

review.rename(columns={'points': 'score'}) for renaming coloumns
review.rename(index={'0': 'firstentry'}) for renaming indexs

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

used to rename rows and coloumn header names    


joining and concatenating

Concatenating
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv") 
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

Joining
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')