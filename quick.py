class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None
class linkedlist():
    def __init__(self):
        self.head = None
    def print_ll1(self):
        if self.head is None:
            print("linkedlist is empty...")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head=self.head.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_btwn(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not available")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

ll1 = linkedlist()
ll1.add_begin(10)
ll1.add_begin(50)
ll1.add_end(30)
ll1.add_end(70)
ll1.add_btwn(50,10)
ll1.print_ll1()