spaces=[7]
#class of binary search tree
class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
#insert method to insert the element
    def insert(self, data):
        #if there is no element in the tree
        if self.key is None:
            self.key = data#assigning that element to be the key
            return
        elif self.key == data:#If there are duplicate elements
            return
        elif self.key > data:#To assign the left child
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BST(data)  # Bst is called to create a new node
        else:#To assign the right child
            if self.right_child:
                self.right_child.insert(data)
            else:#creating a node if there is not a node
                self.right_child = BST(data)
#searching an element from the tree
    def search(self, data):
        if self.key == data:#If the element is found at the root itself
            print("Element is Found")
            return
        elif data < self.key:#if the element is less than the root them traversing through the left child
            if self.left_child:
                self.left_child.search(data)#recursion to search again
            else:#If the element is not found
                print("Node is not present in tree")
        else:#if the element is greater than the root then traversing through the left child
            if self.right_child:
                self.right_child.search(data)
            else:
                print("Node is not present in tree")

def print2DUtil(root, space):#To print like a tree
        # Base case
        if (root == None):
            return
        # Increase distance between levels
        space += spaces[0]
        # Process right child first
        print2DUtil(root.right_child, space)
        # Print current node after space
        # count
        print()
        for i in range(spaces[0], space):
            print(end=" ")
        print(root.key)
        # Process left child
        print2DUtil(root.left_child, space)
#printing the root node first
def print2D(root):
    print2DUtil(root, 0)
#user input for root node's value
key = int(input("Enter the root node of the tree: "))
#object instantiation
root = BST(key)
print2DUtil(root ,0)
#user input for total number of elements to be inserted
n = int(input("Enter the total number of element to be inserted excluding root node: "))
#for loop to get the required number of elements
for i in range(n):
    ele = int(input("Element {}:".format(i + 1)))
    root.insert(ele)
    #displaying the tree representation after each iteration
    print("Tree Representation from left to right:")
    print2D(root)
#user input to search the element
c = int(input("Enter the element to be searched: "))
root.search(c)