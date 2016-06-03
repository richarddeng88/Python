import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import urllib

##### loading data from files
# x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)
#
# plt.plot(x,y, label= 'loading data from files')
#
# plt.title('loading data from files')
# plt.legend()
# plt.show()

## loading data from internet

def gra(stock):
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+ '/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data =[]
    split = source_code.split('\n')

    for line in split:
        split_line = line.split(",")
        if len(split_line) == 6:
            if 'value' not in line:
                stock_date.append()

    date,closep, highp, lowp, openp, volumn = np.loadtxt(stock_data,
                                                         delimiter=",",
                                                         unpack=True,
                                                         # %Y= full year, 2015, %y = partial year 15
                                                         # %m = number month, %d = number day
                                                         # %H=  hours
                                                         converters={0: bytespdate2num('%Y%m%d')})


# gra('TSLA')















