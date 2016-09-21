#A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings,
# using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.
#The module re provides full support for Perl-like regular expressions in Python.

#The match Function
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
print matchObj
print type(matchObj)

# We use group(num) or groups() function of match object to get matched expression.
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"












