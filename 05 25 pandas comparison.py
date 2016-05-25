import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import quandl
import html5lib
import lxml
import pickle
style.use('fivethirtyeight')

height = {'meters':[10.25,10.31,10.27,10.22,7364.2,10.28,10.24,10.35]}

df= pd.DataFrame(height)
df['std'] = pd.rolling_std(df['meters'],2)
df_std = df.describe()['meters']['std']
print(df_std)

df2 = df[(df['std']<df_std)]
print(df2)

df2.plot()
plt.show()














