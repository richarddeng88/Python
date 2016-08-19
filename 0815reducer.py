#!/usr/bin/python2.6

import sys

highest = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue  ## continue statement continues with the next iteration of the loop:

    thisKey, thisSale = data

    if oldKey and oldKey != thisKey:
        print "{0} {1}".format(oldKey, highest)
        highest = 0

    oldKey = thisKey
    if thisSale >= highest:
        highest = float(thisSale)

        # if oldKey != None:
        #    print oldKey, "\t", salesTotal
