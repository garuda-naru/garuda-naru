Write a Python program to create a singly linked list, append some items and iterate through the list.





class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
class Single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def iter(self):
        n = self.head
        while n:
            val = n.data
            n = n.next
            yield val
    def append(self,data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count+=1
l = Single_linked_list()
l.append("Python")
l.append("Java")
l.append("HTMl")
l.append("JavaScript")
l.append("Cloud Computing")
l.append("Networking")
l.append("AutoCad")
for i in l.iter():
    print(i,"-->",end=" ")
print()
print("Head : ",l.head.data)
print("Tail : ",l.tail.data)
print(l.count)
