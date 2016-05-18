import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as style
import numpy as np
import quandl
import html5lib
import lxml
import pickle

api_key ="-tu16JxTi3ZC9D4CPXCZ"
##price = quandl.get("FMAC/HPI_MUNIN", start_date="1990-01-31",authtoken=api_key)
##states  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
##a = states[0]
##
##main_df = pd.DataFrame()
##
##for abbv in states[0][0][1:]:
##      query = 'FMAC/HPI_' + str(abbv)
##      df = quandl.get(query,start_date="1990-01-31",authtoken=api_key)
##      df.columns = [str(abbv)]
##      print 'get file from ' + query
##      if main_df.empty :
##                   main_df = df
##      else:
##                   main_df = main_df.join(df)
##      print 'successful'



def state_list():
        fstates  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
        return fstates[0][0][1:]

def grab_initial_state_date():
        states = state_list()
        main_df = pd.DataFrame()
        print "get the data"
        for abbv in states:
                query = 'FMAC/HPI_'+ str(abbv)
                df = quandl.get(query,start_date="1990-01-01",authtoken=api_key)
                df.columns = [str(abbv)]
                print 'get file from ' + query
                if main_df.empty :
                             main_df = df
                else:
                             main_df = main_df.join(df)
                print 'successful'

        print(main_df.head())

        pickle_out = open('fstates.pickle','wb')
        pickle.dump(main_df, pickle_out)
        pickle_out.close()


grab_initial_state_date()

pickle_in = open('fstates.pickle','rb')
hpi_data = pickle.load(pickle_in)
print hpi_data.head()



## fast way to send data frame to pickle in pandas
## auusme we had a dataset hpi_data
hpi_data.to_pickle('pickllle')
df = pd.read_pickle('pickllle')

################## modifying columns
# add a new column
plt.style.use('fivethirtyeight')
df['TX2'] = df['TX']*2
df.plot()
plt.legend().remove()
plt.show()

























