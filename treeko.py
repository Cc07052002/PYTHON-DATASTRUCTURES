class TreeNode(object):
    def __init__(self, val):
        self.val = val#value of the root node
        self.left = None#left child
        self.right = None#right child
        self.height = 1#


# AVL tree class including insertion
class AVL_Tree(object):

    # Recursive function to insert key in the subtree rooted 
    def insert(self, root, key):

        #Performing  normal Binary Search Tree
        if not root:
            return TreeNode(key)
        elif key < root.val:#
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the previous node
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced then trying the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)

        # If the tree has only one node, then return it
        if root is None:
            return root

        # Update the height of the previous node
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        #Get the balance factor
        balance = self.getBalance(root)

        #If the node is unbalanced then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    #method to left rotate
    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        #updating the height
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        #Return the new root
        return y
    #method of right rotate
    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Updating height
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        # Return the new root
        return y
    
    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
#method to print the tree
def print2DUtil(root, space):  # To print like a tree
        # Base case
        spaces = [7]
        if (root == None):
            return
        # Increase distance between levels
        space += spaces[0]
        # Process right child first
        print2DUtil(root.right, space)
        # Print current node after space
        # count
        print()
        for i in range(spaces[0], space):
            print(end=" ")
        print(root.val)
        # Process left child
        print2DUtil(root.left, space)


# printing the root node first
def print2D(root):
    print2DUtil(root, 0)


# Driver code
myTree = AVL_Tree()
root = None
myTree.getBalance(root)

n = int(input("Enter the total number of nodes to be inserted: "))
#for loop to get the required number of elements
for i in range(n):
    ele = int(input("Value to be inserted {}:".format(i + 1)))
    root = myTree.insert(root, ele)

    #displaying the tree representation after each iteration
    print("Tree Representation from left to right:")
    print2D(root)
    print("The balance value of the tree: ")
    print(myTree.getBalance(root))
#user input to search the element
c = int(input("Enter the number of nodes to be deleted: "))
for i in range(c):
    ele = int(input("Value to be deleted {}:".format(i + 1)))
    root = myTree.delete(root,ele)
    print("Tree Representation from left to right:")
    print2D(root)
    flag=int(input("Do you want to check the balance 1.Yes"))
    if flag==1:
       print(myTree.getBalance(root))



