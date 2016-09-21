class SetofStacks:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print items

s = SetofStacks()
print s.isEmpty()
s.push("rich")
s.printstack()
s.push("ob")
print 'try...............1'
s.printstack()
s.pop()
print 'try...............2'
s.printstack()