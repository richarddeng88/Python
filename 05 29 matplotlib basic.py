import matplotlib.pyplot as plt
# x=[1,2,3]
# y=[5,4,9]
#
# x2 = [1,2,3]
# y2=[12,34,29]
#
# plt.plot(x,y, label='fist line')
# plt.plot(x2,y2,label='second line')
# plt.xlabel('plot number')
# plt.ylabel('important var')
# plt.title('interesting graph \n check it out')
# plt.legend()
# plt.show()

# ############ bar chart
##x= [2, 4 ,6 ,8, 10]
##y= [6,7,8,2,4]
##x2 = [1,3,5,7,9,11]
##y2=[3,4,9,9,3,19]
##plt.bar(x,y, label='bar1',color='blue')
##plt.bar(x2,y2,label='bar2', color='red')
##
##plt.xlabel('x')
##plt.ylabel('y')
##plt.legend()
##plt.show()

# histogram
##population= [22,33,22,34,5,4,33,12,32,12,34,54,34,21,55,33,89,65,43,56,43,24,567,5,3,45,32]
##bins = [0,10,20,30,40,50,60,70,80,90,100]
##plt.hist(population, bins, histtype='bar', rwidth=0.8, label="test")
##plt.legend()
##plt.show()


##### scatter plot
##x= [1,2,3,4,5,6]
##y= [4,5,2,3,7,8]
##plt.scatter(x,y, label="test", color='k', marker='*', s=60)
##plt.legend()
##plt.show()

# #### stack plot
##days=[1,2,3,4,5]
##sleeping = [7,8,6,5,6]
##eating=[2,3,5,4,6]
##working=[4,5,8,7,5]
##
##plt.plot([],[], color= 'r', label='eating',linewidth=5)
##plt.plot([],[], color= 'g', label='sleeping',linewidth=5)
##plt.plot([],[], color= 'b', label='working',linewidth=5)
##
##plt.stackplot(days, sleeping, eating, working)
##plt.title('stack plot')
##plt.xlabel('days')
##plt.ylabel('activity')
##plt.legend()
##plt.show()



#### pie chart
slices = [7,2,13]
activities = ['sleep', 'eating','working']
color = ['c','m','b']

plt.pie(slices,
        labels = activities,
        colors=color,
        startangle=60,
        shadow=True,
        explode=(0,0.3,0.1),
        autopct='%1.1f%%')
plt.title('stack plot')
plt.show()




