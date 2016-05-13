import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as style
import numpy as np
import quandl

# BASICS
web = {'day':[1,2,3,4,5,6],
       'visitor':[11, 12, 13 , 14,15, 16],
       'rate':[21,22,23,24,25,26]
    }

df =  pd.DataFrame(web)
#print df.head(2)

df2 = df.set_index('day')
#print df2

#print df['visitor']
#print df.visitor
#print df[['visitor','rate']]
print df.visitor.tolist()
print np.array(df[['visitor','rate']])

# IO
mydata = quandl.get("ZILL/Z11373_MPC")
#df = pd.read_csv('ZILL-Z11373_MPC.csv')
#df.to_csv('newdf.csv')
#df = pd.read_csv('ZILL-Z11373_MPC.csv', index_col=0)
#df.columns = ['House Price in Elmhurst']
#df = pd.read_csv('ZILL-Z11373_MPC.csv', names=['Date','elmhurst price'],index_col=0)
#df.to_html('example.html')

# building dataset





































