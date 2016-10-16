import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as style
import numpy as np
import quandl
import html5lib
import lxml
import pickle
plt.style.use('fivethirtyeight')

df = pd.read_pickle('pickllle')
################## modifying columns
# add a new column
df['TX2'] = df['TX']*2
ax1 = plt.subplot2grid((1,1),(0,0))
ax2 = plt.subplot2grid((2,1),(0,0), sharex=ax1)
##df.plot()
##plt.legend().remove()
##plt.show()


##a = df['NY']
##a = a.pct_change()
##a.plot()
##plt.show()

##NY1yr = df['NY'].resample('A', how='mean') # resample hourly, put "H", daily, put "D"
                                # yearly/anually , put "A"
##print(NY1yr.head())

##NY1yr.plot(ax=ax1, label='yearly ny hpi')
##df['NY'].plot(ax=ax1, label='monthly ny hpi')
##plt.legend(loc=4)
##plt.show()



# dealing with miss value
##df['ny1yr'] = df['NY'].resample('A').mean() # there are a lot of missing values.
#df.dropna(inplace= True)  # delete all row with NA
##df.fillna(method='bfill', inplace=True)
##print df[['NY','ny1yr']].head()
##df[['NY','ny1yr']].plot(ax=ax1)
##plt.show()

## rolling function
#df['new'] = pd.rolling_mean(df['NY'],12)

c = df['NY'].rolling(window=12, center=False).mean()
df['NY'].plot(ax=ax1, label='monthly ny hpi')
c.plot(ax=ax2)
plt.show()































