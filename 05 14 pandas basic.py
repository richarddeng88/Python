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
price = quandl.get("FMAC/HPI_MUNIN", start_date="1990-01-31",authtoken=api_key)
states  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
a = states[0]

main_df = pd.DataFrame()

for abbv in states[0][0][1:]:
	query = 'FMAC/HPI_'+ str(abbv)
	name = str(abbv)
	df = quandl.get(query,start_date="1990-01-31",authtoken=api_key)
	df.columns = [str(abbv)]
	print 'get file from ' + query
	if main_df.empty :
		     main_df = df
	else:
		     main_df = main_df.join(df)
	print 'successful'



##def state_list():
##	states  =  pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
##	return states[0][0][1:]
##
##def grab_initial_state_date():
##	states = state_list()
##	main_df = pd.DataFrame()
##
##for abbv in states:
##	query = 'FMAC/HPI_'+ str(abbv)
##	name = str(abbv)
##	df = quandl.get(query,start_date="1990-01-31",authtoken=api_key)
##	df.columns = [str(abbv)]
##	print 'get file from ' + query
##	if main_df.empty :
##		     main_df = df
##	else:
##		     main_df = main_df.join(df)
##	print 'successful'
##





































