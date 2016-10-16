import sys
import pandas as pd

### program output and input
# %s means to substitute a tring; %d means to substitute an integer
print "%s is number %d" % ("python", 1)

#user = raw_input("enter your login name: ")
#print 'your login is: ', user

sq = [x ** 2 for x in range(4)]
print sq
for i in sq:
    print i

states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
print type(states)
print type(states[0])
print states[0].head()

