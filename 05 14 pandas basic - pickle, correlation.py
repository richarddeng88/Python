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
                #df = quandl.get(query,start_date="1990-01-01",authtoken=api_key)
                df = quandl.get(query,authtoken=api_key)
                df.columns = [str(abbv)]
                df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] *100
                
                print 'get file from ' + query
                if main_df.empty :
                             main_df = df
                else:
                             main_df = main_df.join(df) # ADD A NEW COLUMN
                print 'successful'

        print(main_df.head())
        pickle_out = open('fstates.pickle','wb') # save into a pickle file
        pickle.dump(main_df, pickle_out)
        pickle_out.close()


##grab_initial_state_date()

pickle_in = open('fstates.pickle','rb')
hpi_data = pickle.load(pickle_in)
##print hpi_data.head()


## this is the usa whole market house price data 
def hpi_benchmark():
        df= quandl.get("FMAC/HPI_USA",authtoken=api_key)
        df.columns =['usa']
        df['usa'] = (df['usa'] - df['usa'][0]) / df['usa'][0] *100
        print('usa data is ready to analze')
        print(df.head())
        return df

benchmark = hpi_benchmark()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

## fast way to send data frame to pickle in pandas
## auusme we had a dataset hpi_data
hpi_data.to_pickle('pickllle') # save data to pickle
df = pd.read_pickle('pickllle') # read data from a pickle

################## modifying columns
# add a new column
plt.style.use('fivethirtyeight')
#df['TX2'] = df['TX']*2

##df.plot(ax=ax1)
##benchmark.plot(ax=ax1, color='k',linewidth=10)
##plt.legend().remove()
##plt.show()

hpi_data_correlation = hpi_data.corr()  #cor() in R
print hpi_data_correlation.describe()  # summary() in R
                # we found out the every state is strongly corrlated with each other

























