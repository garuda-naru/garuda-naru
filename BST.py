#Create Binary Search Tree Class
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
#Create a Function For Updating a Value
    def insert(self, data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if  self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
#Create a Function for Searching a Value
    def searching (self,data):
        if self.key == data:
            print("Node Found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.searching(data)
            else:
                print("Node Not Found!")
        else:
            if self.rchild:
                self.rchild.searching(data)
            else:
                print("Node not Found!")
#Traversal for Pre order
    def porder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.porder()
        if self.rchild:
            self.rchild.porder()
#Traversal for Inorder
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
#Traversal for Postorder
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
#Finding Minimum Value
    def min_val(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(current.key)
#Finding Max Value
    def max_val(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(current.key)
        
r = BST(None)
list1 = [0,9,3,4,8,5,1,7,6,3,2,4,8,9,4,5,7,9,1]
for i in list1:
    r.insert(i)
r.searching(2)
r.porder()
print("Preorder")
r.inorder()
print("In order")
r.postorder()
print("Post Order")
r.min_val()
print("Min Value")
r.max_val()
print("Max Value")