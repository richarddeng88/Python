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
df.plot()
plt.legend().remove()
plt.show()


a = df['NY']
a = a.pct_change()
a.plot()
plt.show()
