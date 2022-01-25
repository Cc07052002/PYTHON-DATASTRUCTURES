# creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # function for traversing array in forward direction
    def printForward(self):
        print("Linked List traversing in forward direction.")
        print()
        temp = self.head
        while (temp):
          print(temp.data, end=' ')
          temp = temp.next

    # function for traversing array in reverse direction
    def printReverse(self,temp):
        if temp:
            self.printReverse(temp.next)
            print(temp.data, end=' ')
        else:
            return

    # function to insert elements at the end
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = node

    # function to insert elements at the beginning
    def insertFirst(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node

    # function to insert elements at the desired location
    def insertPos(self, position, data):
        first = self.head

        # This condition to check whether the
        # position given is valid or not.
        if (position < 1):
            print("Invalid position!")

        if position == 1:
            newNode = Node(data)
            newNode.next = first
            first = newNode

        else:

            # Keep looping until the position is zero
            while (position != 0):
                position -= 1

                if (position == 0):
                    # adding Node at required position
                    newNode = Node(data)
                    newNode.next = first.next
                    first.next = newNode
                    break

                first = first.next
                if first == None:
                    break



# getting elements in the linked list using for loop
LL = LinkedList()

for i in range(1, 11):
    LL.insert(int(input("Enter the data for {} node -> ".format(str(i)))))
print()
# printing list in forward direction
LL.printForward()
print()
# printing list in reverse direction
print()
print("Linked List traversing in reverse direction.\n")
LL.printReverse(LL.head)
print()
# getting choice from the user
print("\nYour choices to perform operatrion \n\t1] Insert at the end.\n\t2] Insert at the begining.\n\t3] Insert at the middle.\n\t4] Quit")
# checking the choice and calling the desired function
while True:
    choice = int(input('\nEnter the number of your choice -> '))
    if (choice not in range(1, 5)):
        print("Choose from the given numbers.")
    elif choice == 1:
        val = int(input('\nEnter the value to be inserted in the end -> '))
        LL.insert(val)
        LL.printForward()
    elif choice == 2:
        val = int(input('\nEnter the value to be inserted in the begining -> '))
        LL.insertFirst(val)
        LL.printForward()
    elif choice == 3:
        val = int(input('\nEnter the value to be inserted -> '))
        position = int(input('Enter the position to be inserted -> '))
        LL.insertPos(position, val)
        LL.printForward()
    elif choice == 4:
        break