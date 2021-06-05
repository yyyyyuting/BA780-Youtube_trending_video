# -*- coding: utf-8 -*-
"""Team 6A BA780.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NSoHaJGt9Nzhr0eNbk3Tq1Q2t7Wu5_aY

## **Phase 2 Bruce's Part**
"""

import pandas as pd
import seaborn as sns
data1=pd.read_csv('YouTube Trending Videos dataset.csv')
data2=data1[['trending_date','Country', 'Category_name', 'view_count']]
data2['year']= pd.DatetimeIndex(data2['trending_date']).year

data2

"""###a. Top 10 Categories in the Japan in 2018"""

data5=data2.loc[(data2["Country"] == "Japan") & (data2["year"] == 2018)]
top_jp_2018=data5[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=False)[0:10].reset_index(level='Category_name')
pd.DataFrame(top_jp_2018)

"""###a. Top 10 Categories in the Japan in 2020"""

data6=data2.loc[(data2["Country"] == "Japan") & (data2["year"] == 2020)]
top_jp_2020=data6[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=False)[0:10].reset_index(level='Category_name')
pd.DataFrame(top_jp_2020)

"""###a. Top 10 Categories in the United states in 2018"""

data3=data2.loc[(data2["Country"] == "United States") & (data2["year"] == 2018)]
top_us_2018=data3[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=False)[0:10].reset_index(level='Category_name')
pd.DataFrame(top_us_2018)

"""###a. Top 10 Categories in the United states in 2020"""

data4=data2.loc[(data2["Country"] == "United States") & (data2["year"] == 2020)]
top_us_2020=data4[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=False)[0:10].reset_index(level='Category_name')
pd.DataFrame(top_us_2020)

"""###b. Top 10 categories of the US in 2018 VS Top 10 categories of Japan in 2018

> Are top 10 categories from two countries the same?
"""

top_jp_2018['Japan']='v'
jp2018=pd.DataFrame(top_jp_2018[['Category_name', 'Japan']])
top_us_2018['United States']='v'
us2018=pd.DataFrame(top_us_2018[['Category_name', 'United States']])
jp2018.merge(us2018, on='Category_name', how='outer')

"""> In the top 10, compare view count from Japan to the US"""

jp2018_2= pd.DataFrame(top_jp_2018[['Category_name', 'view_count']])
jp2018_3=jp2018_2.rename(columns={'view_count':'Japan_view_count'})
jp2018_3
us2018_2= pd.DataFrame(top_us_2018[['Category_name', 'view_count']])
us2018_3=us2018_2.rename(columns={'view_count':'US_view_count'})
us2018_3
jp2018_3.merge(us2018_3, on='Category_name', how='outer')

"""###b. Top 10 categories of the US in 2020 VS Top 10 categories of Japan in 2020

> Are top 10 categories from two countries the same?
"""

#Bug: replace NaN with x
top_jp_2020['Japan']='v'
jp2020=pd.DataFrame(top_jp_2020[['Category_name', 'Japan']])
top_us_2020['United States']='v'
us2020=pd.DataFrame(top_us_2020[['Category_name', 'United States']])
jp2020.merge(us2020, on='Category_name', how='outer')

"""> In the top 10, compare view count from Japan to the US"""

#Bug: Change the form of number
jp2020_2= pd.DataFrame(top_jp_2020[['Category_name', 'view_count']])
jp2020_3=jp2020_2.rename(columns={'view_count':'Japan_view_count'})
us2020_2= pd.DataFrame(top_us_2020[['Category_name', 'view_count']])
us2020_3=us2020_2.rename(columns={'view_count':'US_view_count'})
jp2020_3.merge(us2020_3, on='Category_name', how='outer')

"""###e. Bottom 10 Categories in the Japan in 2018"""

data5=data2.loc[(data2["Country"] == "Japan") & (data2["year"] == 2018)]
bottom_jp_2018=data5[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=True)[0:10].reset_index(level='Category_name')
pd.DataFrame(bottom_jp_2018)

"""###e. Bottom 10 Categories in the Japan in 2020"""

data6=data2.loc[(data2["Country"] == "Japan") & (data2["year"] == 2020)]
bottom_jp_2020=data6[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=True)[0:10].reset_index(level='Category_name')
pd.DataFrame(bottom_jp_2020)

"""###e. Bottom 10 Categories in the US in 2018"""

data3=data2.loc[(data2["Country"] == "United States") & (data2["year"] == 2018)]
bottom_us_2018=data3[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=True)[0:10].reset_index(level='Category_name')
pd.DataFrame(bottom_us_2018)

"""###e. Botton 10 Categories in the US in 2020"""

data4=data2.loc[(data2["Country"] == "United States") & (data2["year"] == 2020)]
bottom_us_2020=data4[['Category_name', 'view_count']].groupby('Category_name').sum().sort_values(by='view_count', ascending=True)[0:10].reset_index(level='Category_name')
pd.DataFrame(bottom_us_2020)

"""###f. Bottom 10 Categories of the US in 2018 VS Bottom 10 Categories of Japan in 2018

> Are bottom 10 categories from two countries the same?
"""

bottom_jp_2018['Japan']='v'
bottom_jp2018=pd.DataFrame(bottom_jp_2018[['Category_name', 'Japan']])
bottom_us_2018['United States']='v'
bottom_us2018=pd.DataFrame(bottom_us_2018[['Category_name', 'United States']])
bottom_jp2018.merge(bottom_us2018, on='Category_name', how='outer')

"""> In the bottom 10, compare view count from Japan to the US"""

bottom_jp2018_2= pd.DataFrame(bottom_jp_2018[['Category_name', 'view_count']])
bottom_jp2018_3=bottom_jp2018_2.rename(columns={'view_count':'Japan_view_count'})
bottom_us2018_2= pd.DataFrame(bottom_us_2018[['Category_name', 'view_count']])
bottom_us2018_3=bottom_us2018_2.rename(columns={'view_count':'US_view_count'})
bottom_jp2018_3.merge(us2018_3, on='Category_name', how='outer')

"""###f. Bottom 10 Categories of the US in 2018 VS Bottom 10 Categories of Japan in 2020

> Are bottom 10 categories from two countries the same?
"""

bottom_jp_2020['Japan']='v'
bottom_jp2020=pd.DataFrame(bottom_jp_2020[['Category_name', 'Japan']])
bottom_us_2020['United States']='v'
bottom_us2020=pd.DataFrame(bottom_us_2020[['Category_name', 'United States']])
bottom_jp2020.merge(bottom_us2020, on='Category_name', how='outer')

"""> In the bottom 10, compare view count from Japan to the US"""

bottom_jp2020_2= pd.DataFrame(bottom_jp_2020[['Category_name', 'view_count']])
bottom_jp2020_3=bottom_jp2020_2.rename(columns={'view_count':'Japan_view_count'})
bottom_us2020_2= pd.DataFrame(bottom_us_2020[['Category_name', 'view_count']])
bottom_us2020_3=bottom_us2020_2.rename(columns={'view_count':'US_view_count'})
bottom_jp2020_3.merge(bottom_us2020_3, on='Category_name', how='outer')