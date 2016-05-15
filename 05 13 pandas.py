import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as style
import numpy as np
import quandl
import html5lib
import lxml

# Data Frame
web = {'day':[1,2,3,4,5,6],
       'visitor':[11, 12, 13 , 14,15, 16],
       'rate':[21,22,23,24,25,26]
    }

df =  pd.DataFrame(web)
#change the column names
df.columns = ['a','b','c']
#set up the index
df2 = df.set_index('a')
#read the specific column
df['a']
df.a
df[['a','b']]
df.a.tolist()
np.array(df[['a','b']])

# IO - pandas read data function
mydata = quandl.get("ZILL/Z11373_MPC")
df = pd.read_csv('ZILL-Z11373_MPC.csv')
df.to_csv('newdf.csv')
df = pd.read_csv('ZILL-Z11373_MPC.csv', index_col=0)
df.columns = ['House Price in Elmhurst']
df = pd.read_csv('ZILL-Z11373_MPC.csv', names=['Date','elmhurst price'],index_col=0)
df.to_html('example.html')

# building dataset
# api_key = open('api key.csv','r').read()
price = quandl.get("FMAC/HPI_MUNIN", start_date="1990-01-31")
states  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
a = states[0]
for abbv in states[0][0] :
     print 'FMAC/HPI_'+ str(abbv)
names = states[0][0]


# concatenating and appending dataframes
df1 = pd.DataFrame({'hpi':[80,85,88,85],
                    'int_rate':[2,3,2,2],
                    'us_gdp_thousands':[50,55,65,55]},
                   index = [2001,2002,2003,2004])

df2 = pd.DataFrame({'hpi':[80,85,88,85],
                    'int_rate':[2,3,2,2],
                    'us_gdp_thousands':[54,51,44,43]},
                   index = [2005,2006,2007,2008])

df3 = pd.DataFrame({'hpi':[80,85,88,85],
                    'unemployment':[7,8,9,6],
                    'lower_tier':[50,55,65,55]},
                   index = [2001,2002,2003,2004])

concat= pd.concat([df1, df2,df3])
df4 = df1.append(df2)
s = pd.Series([180,299,150], index=['hpi','int_rate','us_gdp_thousands'])
df5 = df1.append(s,ignore_index=True)

# joining and merging dataframes
df6 = pd.merge(df1,df2,on=['hpi','int_rate'])

df1.set_index('hpi',inplace=True)
df3.set_index('hpi',inplace=True)

joined = df1.join(df3)


df1 = pd.DataFrame({'year':[2001,2002,2003,2004],
                    'int_rate':[2,3,2,2],
                    'us_gdp_thousands':[50,55,65,55]})

df2 = pd.DataFrame({'year':[2001,2002,2003,2005],
                    'int_rate':[2,3,2,2],
                    'us_gdp_thousands':[54,51,44,43]})

merge = pd.merge(df1,df2, on='year', how='right')# right, right, outer, inner(default)
merge.set_index('year',inplace=True)






















