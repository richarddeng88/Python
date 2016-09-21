import time

# time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

#To translate a time instant from a seconds since the epoch floating-point value into a time-tuple,
# pass the floating-point value to a function
localtime = time.localtime(time.time())
print "Local current time :", localtime

## format the time
#You can format any time as per your requirement, but simple method to get time in readable format is asctime()
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


#######Getting calendar for a month
import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal




