import threading
import time
import datetime

def printit():
    current_time = datetime.datetime.now()
    threading.Timer(1, printit).start()
    add_info("richard,the time is ")
    add_info(str(current_time))
    print "richard, the current time is ", current_time
    add_info("\n")


def add_info(name):
   hs = open("hst.txt","a")
   hs.write(name)
   hs.close()

printit()