##
a=str(2) #here str() transfer the numeric to charater
type(a)

## import a module named "time"
import time
print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))

# list basic
myfears = ["high","distance", "afraid"]

print myfears[0], myfears[1]

print len(myfears)
print len(myfears[2])

# list slicing
mylist = [1,2,3,4,5 ,6,7,8,9,10]
#print mylist[0]
#print mylist[1]
#print mylist[-1]
#print mylist[2:]
#print mylist[:5]
#print mylist[3:7]

# list methods : list append, insert, remove, extend, delete
greet = ['how', 'are','you']
greet.append(',richard')
print greet
greet.insert(2,'good')
print greet
greet.remove('how')
print greet

# load data
book = open('hst.txt')
print type(book)
booktex = book.readlines()
print booktex[0:1]
print type(booktex)
print len(booktex)
print ''
# wirte files
mytext = "i wrote a great article today!"
outfile=open('myarticle.txt','w')
outfile.writelines(mytext)
outfile.close()

# intro to loops
greet = ['how', 'are','you']
for item in greet:
    print item
for qing in greet:
    print qing

    
# conditional loops
myage=28
death=30

while myage < death:
    print 'when i am', myage, 'i will still love my website'
    myage +=1

print 'but when i am' , myage , 'i will die.'


# logics
print 8==2 and 8>7
print 8==2 or 8>7

# if - conditional and logics
number=700
if number/100 == 8 :
    print 'it is 800'
else:
    print 'it is not 800'


# elif
driving_age = 16
smoking_age = 18
lotto_age=19
drinking_age=21

age= int(raw_input('how old are you?'))
        
if age > drinking_age :
        print 'you can drive, moke, gamble, and drink :)'
elif age > lotto_age :
        print 'you can drive, smoe, and gamble'
elif age > smoking_age :
        print 'you can drive and smoke'
elif age > driving_age :
        print 'you can drive :('
else :
    print 'you cannot even drive'

# define a function ( intro)
def get_legal(age):  
    if age > drinking_age :
            print 'you can drive, moke, gamble, and drink :)'
    elif age > lotto_age :
            print 'you can drive, smoe, and gamble'
    elif age > smoking_age :
            print 'you can drive and smoke'
    elif age > driving_age :
            print 'you can drive :('
    else :
        print 'you cannot even drive'








































