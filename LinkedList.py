class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_ll(self):
        n = self.head
        if n is None:
            print("Linkedlist is Empty")
        else:
            while n is not None:
                print(n.data)
                n=n.ref
# If Linked list Empty insert Node Otherwise print LL is Not Empty
    def insert_mt(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linkedlist Not Empty...")
#add New Node at begining of linkedlist
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
#add New Node at The End of Linkedlist
    def add_end(self,data):
        n = self.head
        new_node = Node(data)
        if n is None:
            n= new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node 
#Using particular node we can insert after that node
    def add_after(self,data,x):
        n = self.head
        new_node = Node(data)
        if n is None:
            n = new_node
        else:
            while n is not None:
                if x == n.data:
                    break
                n = n.ref
            if n is None:
                print("Node Not Found..")
            else:
                new_node.ref = n.ref
                n.ref = new_node
#add new Node before a particular Node
    def add_before(self,data,x):
        n = self.head
        new_node = Node(data)
        if n is None:
            n = new_node
        else:
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref
            if n is None:
                print("Node not found")
            else:
                new_node.ref = n.ref
                n.ref = new_node


l = Linkedlist()
l.insert_mt(20)
l.add_begin(30)
l.add_end(50)
l.add_begin(40)
l.add_end(90)
l.add_after(100,50)
l.add_before(500,50)
l.print_ll()