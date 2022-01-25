import sys

# class of singly linked list
class Node:
    def __init__(self, data):
        # Assigning two attributes one to the next node and other to the data in it.
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def if_it_is_empty(self):
        #returning the result of the boolean statement
        return self.front == None

    def enQueue(self, item):
        #create a temp node with attribute item
        temp = Node(item)
        if self.rear == None:
            #both rear and front are the same as only 1 element is there
            self.front = self.rear = temp
            return
        #we are pointing the current last node to the new node
        self.rear.next = temp
        #we are assigning the new node to the rear
        self.rear = temp

    def deQueue(self):
        if self.if_it_is_empty():
            print("The queue is empty")
            return
        #we are assigning the temp to the front node
        temp = self.front
        #we are assigning the next node to be the front
        self.front = temp.next
        if (self.front == None):
            #if the front node is itself none then the rear would be none
            self.rear = None
        return temp.data

    def display(self):
        if self.if_it_is_empty():
            return
        #to print it from first element
        temp = self.front
        while temp:
            #if there only 1 element we dont need a comma or space
            if(temp.data == self.rear.data):
              print(temp.data,end="")
              temp=temp.next
            else:
            #if there are many elements and we need to print it in a comma seperated way
              print(temp.data, end="")
              print(" ,",end="")
              temp = temp.next


class Queue_array:
    def __init__(self):
        #initializing the queue
        self.queue = []
        #initializing the front and rear as 0
        self.front=self.rear=0
    #isempty method to check whether it is empty
    def isEmpty(self):
        return len(self.queue) == 0
    #method of enqueue
    def enQueue(self, data):
            self.queue.append(data)
    #method of dequeue
    def deQueue(self):
        #if the queue is empty
        if len(self.queue)== 0:
            print("Empty Queue")
        else:
            #removing the 1st element according to the principle FIFO
            x = self.queue.pop(0)
            return x

# object instantiation
qll = Queue()

qarr = Queue_array()

choice = 0
while (choice != 3):
    # Getting the choice from the user
    choice = int(input("Enter your choice to perform:\n1 for Queue using Array\n2 for Queue using Linked List\n3 to exit\nYour choice: "))
    # if user enter choice 1 to perform queue on array
    if (choice == 1):
        while (True):
            el = int(input("1 for Enqueue\n2 for Dequeue\n3 To go back to the previous menu\n4 To exit \nYour choice: "))
            if (el == 1):
                element = int(input("Enter Element to Enqueue in Queue\n"))
                qarr.enQueue(element)
                print(qarr.queue)
            elif (el == 2):
                print("The dequeued value is :", qarr.deQueue())
                print("Queue after deQueuing is", qarr.queue)
            elif (el == 3):
                break
            elif (el == 4):
                sys.exit()
            else:
                print("Invalid choice,Please enter a valid choice.")

    # if user enter choice as 2 to perform queue in linked list
    if (choice == 2):
        while True:
            ch = int(
                input("1 for Enqueue\n2 for Dequeue\n3 To go back to the previous menu\n4 To exit \nYour choice: "))
            if (ch == 1):
                c = int(input("Enter the element u want to enqueue: "))
                qll.enQueue(c)
                print("[", end="")
                qll.display()
                print("]")
            elif (ch == 2):
                print("The dequeued value is :", qll.deQueue())
                print("Queue after deQueuing is [", end="")
                qll.display()
                print("]")
            elif (ch == 3):
                break
            elif ch == 4:
                sys.exit()
            else:
                print("Invalid choice,Please enter a valid choice.")
    # To exit the program
    if (choice == 3):
        sys.exit()
    # To display invalid input
    if (choice > 3 or choice < 1):
        print("Invalid choice,Please enter a valid choice.")
