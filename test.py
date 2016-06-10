from threading import Thread
import urllib
import re
import MySQLdb


# conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="citibike")
# c = conn.cursor()
# c.execute("select * from trips_raw limit 100")
# rows = c.fetchall()
# for i in rows:
#     print i;



# def th(ur):
#     regex = "<title>.+?</title>"
#     pattern = re.compile(regex)
#     htmltext = urllib.urlopen(ur).read()
#     results = re.findall(pattern, htmltext)
#     print results
# urls = "http://www.google.com http://www.cnn.com http://www.yahoo.com http://www.wikipedia.com".split()
# threadlist = []
# for u in urls:
#     t = Thread(target=th, args=(u,))
#     t.start()
#     threadlist.append(t)
# for b in threadlist:
#     b.join()

## request result form yahoo finance
gmap = {}
def th(ur):
    base = "http://finance.yahoo.com/q?s=" + ur
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base).read()
    results = re.findall(pattern, htmltext)
    #print "the price of " + str(ur) + " is " + str(results[0])
    try:
        gmap[ur] = results[0]
    except:
        print "got an error"

symbol_list = open("symbol.txt").read()
symbol_list = symbol_list.split("\n")

threadlist = []
for u in symbol_list[0:10]:
    t = Thread(target=th, args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="stocks")

for key in gmap.keys():
    print key, gmap[key]
    x = conn.cursor()
    query = "INSERT INTO stocks.symbol (stock_names, last_price) VALUES ("
    query = query + "'" +key +"'," + gmap[key] + ")"
    x.execute(query)
    rows = x.fetchall()
    conn.commit()

# select the table
x = conn.cursor()
x.execute("select count(*) as num from symbol")
rows = x.fetchall()
print rows