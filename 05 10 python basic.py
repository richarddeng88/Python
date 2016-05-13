names = [['rich',29],['tony',17],['zara',19]]
print type(names)
print names[0][0]

x =[1,2,3]
y = list(x)  # becareful the difference btw y=x and y =list(x)
y[0]=999   
print x

# methods, in python, everything = object
# objects have methods associated, denpending on type
my =[ 'mom',57, 'dad',58,'qing',29]
print my.index('qing')

a="sister"
a.index('t')
a = a.replace('s','bo')
