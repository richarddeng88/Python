class Employee:
    #The variable empCount is a class variable whose value is shared among all instances of a this class.
    # This can be accessed as Employee.empCount from inside the class or outside the class.
    empCount = 0

    #The first method __init__() is a special method, which is called class constructor or initialization method that
    # Python calls when you create a new instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # you declear other class methods like normal functions with the exception that the first argument to each method is self.Python
    # adds the self argument to the list for you; you do not need to include it when you call the methods.
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

##To create instances of a class, you call the class using class name and pass in whatever arguments
# its __init__ method accepts.
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee number is %d" % Employee.empCount


a = Employee('richard', 10000)
a.displayCount()
a.displayEmployee()
a.age = 28
print type(a)


print "Employee.__doc__:", Employee.__doc__ #Class documentation string or none, if undefined.
print "Employee.__name__:", Employee.__name__ #Class name.
print "Employee.__module__:", Employee.__module__ #Module name in which the class is defined.
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__  # Dictionary containing the class's namespace.

######### Destroying Objects (Garbage Collection)
# Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero.
# An object's reference count changes as the number of aliases that point to it changes.


#Class Inheritance

# Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the
# parent class in parentheses after the new class name.
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method











