import urllib
import re

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

symbol_list = ["aapl","spy","goog","nflx",'amzn']
i=0
while i < len(symbol_list):
    urls = "http://finance.yahoo.com/q?s="+ symbol_list[i]+ "&ql=0"
    htmlfile = urllib.urlopen(urls)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+symbol_list[i]+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "the price of ", symbol_list[i],price
    i += 1
