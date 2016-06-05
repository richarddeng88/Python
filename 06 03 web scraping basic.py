import urllib
import re
import json

## in this example, actually we request the entire page and then extract some details from the entire source.

urls = ["http://google.com",
        "http://cnn.com",
        "http://nytimes.com",
        "http://www.yahoo.com",
        "http://www.youtube.com"]

# i = 0
# regex = "<title>(.+?)</title>"
# pattern = re.compile(regex)
#
# while i < len(urls):
#     htmlfile = urllib.urlopen(urls[i])
#     htmltext = htmlfile.read()
#     titles = re.findall(pattern, htmltext)
#     print titles
#     i+=1


# symbol_list = ["aapl","spy","goog","nflx",'amzn']
# i=0
# while i < len(symbol_list):
#     urls = "http://finance.yahoo.com/q?s="+ symbol_list[i]+ "&ql=0"
#     htmlfile = urllib.urlopen(urls)
#     htmltext = htmlfile.read()
#     regex = '<span id="yfs_l84_'+symbol_list[i]+'">(.+?)</span>'
#     pattern = re.compile(regex)
#     price = re.findall(pattern, htmltext)
#     print "the price of ", symbol_list[i],"is", price[0]
#     i += 1



symbol_file = open("symbol.txt")
symbol_list = symbol_file.read()
symbol_list = symbol_list.split("\n")


# for i in symbol_list[1:100]:
#     urls = "http://finance.yahoo.com/q?s="+ i + "&ql=0"
#     htmlfile = urllib.urlopen(urls)
#     htmltext = htmlfile.read()
#     regex = '<span id="yfs_l84_'+ i +'">(.+?)</span>'
#     pattern = re.compile(regex)
#     price = re.findall(pattern, htmltext)
#     print "the price of ", i ,"is", price[0]

# j=1
# for i in symbol_list[1:20]:
#     urls = "http://finance.yahoo.com/q?s="+ i + "&ql=0"
#     htmlfile = urllib.urlopen(urls)
#     htmltext = htmlfile.read()
#     regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'  # any number of character, either upper case or lower case can be accessed here.
#     pattern = re.compile(regex)
#     price = re.findall(pattern, htmltext)
#     print j, "the price of ", i ,"is", price # price[0]
#     j+=1

#### downloading 1 min stock price of appl
# htmltext = urllib.urlopen("http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL%3AUS?timeFrame=1_DAY")
# data = json.load(htmltext)
# print "appl 1 min data"
# print data[0]["price"][2]["value"]
# datapoint = data[0]["price"]
# # for point in datapoint:
# #     print point["value"]
# print "the total number of stock value are ", len(datapoint)

symbol_list = open("symbol.txt").read()
symbol_list = symbol_list.split("\n")

for symbol in symbol_list:
    print symbol
    myfile = open("bloomberg_stock_price/"+ symbol +".txt", "w+" )
    myfile.close()

    htmltext = urllib.urlopen("http://www.bloomberg.com/markets/api/bulk-time-series/price/"+ symbol +"%3AUS?timeFrame=1_DAY")
    data = json.load(htmltext)
    # print data[0]["price"]
    datapoint = data[0]["price"]

    myfile = open("bloomberg_stock_price/" + symbol + ".txt", "a")
    for point in datapoint:
        #print "at ",point["dateTime"],", the price is ",point["value"]
        myfile.write(str(symbol +"," + str(point["dateTime"]) +","+ str(point["value"])+"\n"))
        #myfile.close()




