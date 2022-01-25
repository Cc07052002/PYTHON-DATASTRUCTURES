#defining the class
class Node:
 def __init__(self,data):
    self.prev = None
    self.data = data
    self.next = None
#the class of doubly linked list
class DLL:
    def __init__(self):
        self.head = None
        self.length = 0
    #function for traversing the list in forward direction
    def printForward(self,node):
            print("Traversal in forward direction")
            while node:
                print(node.data, end=' ')
                last = node
                node = node.next
    # function for printing the list
    def print(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            last = node
            node = node.next
            print('\n')
    # function for traversing the list in reverse direction
    def printReverse(self):
        print("Traversal in reverse direction")
        last = self.head
        while last.next:
            last = last.next
        while last:
            print(last.data, end=' ')
            last = last.prev

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

        return

    #function for inserting element at the 1st
    def insertFirst(self, data):
        self.length += 1
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
            self.head = newNode
    #function to display invalid position
    def insertPos(self, position, newElement):
        newNode = Node(newElement)
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode
                if (newNode.next != None):
                    newNode.next.prev = newNode
            else:
                print("\nThe previous node is null.")

                #function for deleting the element
    def deletePos(self, index):
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if (self.head != None):
                self.head.prev = None
        else:
            temp = self.head
            for i in range(1, position):
                if (temp != None):
                    temp = temp.next
            if (temp != None and temp.next != None):
                nodeToDelete = temp.next
                temp.next = temp.next.next
            if (temp.next.next != None):
                temp.next.next.prev = temp.next
            nodeToDelete = None
#creating the doubly linked list
dll = DLL()
for i in range(1, 11):
    dll.insert(int(input("Enter the data for {} node -> ".format(str(i)))))
print()
#traversing the list in forward direction
dll.printForward(dll.head)
print()
#traversing the list in reverse direction
dll.printReverse()
print()
#displaying the choice to perform from the user
print("\nYour choices to perform operatrion \n\t1] Insert at the end.\n\t2] Insert at the begining.\n\t3] Insert at the middle.\n\t4] Delete a Node\n\t5]Quit")
#getting the choice from the user
while True:
    choice = int(input('\nEnter the number of your choice -> '))
    if (choice not in range(1, 6)):#for invalid choice
        print("Choose from the given numbers.")
    elif choice == 1:#for element to insert at the end
        val = int(input('\nEnter the value to be inserted in the end -> '))
        dll.insert(val)
        print("The doubly linked list after inserting the element at the end:")
        dll.print()
    elif choice == 2:#for element to insert at the beginning
        val = int(input("\nEnter the value to be inserted in the begining ->"))
        dll.insertFirst(val)
        print("The doubly linked list after inserting the element at the beginning: ")
        dll.print()
    elif choice == 3:#for element to insert at the middle
        val = int(input('\nEnter the value to be inserted -> '))
        position = int(input("Enter the index of the value to be inserted -> "))
        dll.insertPos(position, val)
        print("The doubly linked list after inserting the element at the ")
        dll.print()
    elif choice == 4:#for deleting an element
        position = int(input("Enter the index of the value to be deleted ->"))
        dll.deletePos(position)
        print("The linkedlist after deleting the value in the givn index number: ")
        dll.print()
    elif choice == 5:#to exit
        break