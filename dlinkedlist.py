#Create a Class for Empty Node
class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
#Linked List Traversal
class Linkedlist:
    def __init__(self):
        self.head = None
#Traversal for forward direction
    def print_f(self):
        if self.head is None:
            print("Linkedlist is Empty...")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.nref
#Traversal for Reverse direction
    def print_r(self):
        print()
        if self.head is None:
            print("Linked list Empty...")
        else:
            n = self.head 
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end="")
                n = n.pref
#Insert a Value if DLL is Empty
    def insert_mt(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not Empty...")
#Insert a Value at The Begining of DLL
    def add_begin(self,data):
        n = self.head 
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
#Insert a Value at The End of Dll
    def add_end(self,data):
        n = self.head
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            while n.nref is not None:
                n=n.nref
            new_node.pref = n
            n.nref = new_node
#Insert a value after a Particular Node
    def add_after(self,data,x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print("Linkedlist is Empty..")
        else:
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node not found")
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
#insert a value before a particular Node
    def add_before(self,data,x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print("Linkedlist is Empty..")
        else:
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node not found")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref  is not None:
                    n.pref.nref=new_node
                else:
                    self.head = new_node
                n.pref = new_node
#Create a Object for Class and call all Functions
l = Linkedlist()
l.insert_mt(50)
l.add_begin(40)
l.add_end(60)
l.add_after(70,60)
l.add_before(500,60)
l.print_f()
l.print_r()
