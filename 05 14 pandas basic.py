import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as style
import numpy as np
import quandl
import html5lib
import lxml
api_key ="-tu16JxTi3ZC9D4CPXCZ"
price = quandl.get("FMAC/HPI_MUNIN", start_date="1990-01-31",authtoken=api_key)
states  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
a = states[0]

main_df = pd.DataFrame()

for abbv in states[0][0][1:]:
	query = 'FMAC/HPI_'+ str(abbv)
	print query
	df = quandl.get(query,start_date="1990-01-31",authtoken=api_key)
	print 'get file from ' + query
	if main_df.empty :
		     main_df = df
	else:
		     main_df = main_df.join(df)
	print 'successful'


##print(main_df.head())
#names = states[0][0]
