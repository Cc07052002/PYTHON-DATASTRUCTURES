import sys
class StackinArray:
  def __init__(self):
    self.stack = []
 #appending element in the stack at the top position
  def push(self, element):
    self.stack.append(element)
    print(self.stack)
    #To pop the last element from the stack
  def pop(self):
    if (not self.isEmpty()):
     lastElement = self.stack[-1]
     del (self.stack[-1])
     return lastElement
    else:
     return ("Stack Already Empty")
     #To check whether the stack is empty or not
  def isEmpty(self):
     return self.stack == []
   #class of singly linked list
class Node:
 def __init__(self, data):
 #Assigning two attributes one to the next node and other to the data in it.
   self.data = data
   self.next = None
class Stack_structure:
 #stack using singly linked list
 def __init__(self):
   self.head = None
 def push_val(self, data):
   if self.head is None:
    self.head = Node(data)
   else:
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
 #poping the last element from the stack
 def pop_val(self):
   if self.head is None:
     return None
   else:
    del_Val = self.head.data
    self.head = self.head.next
    #returning the last element which is popped
    return del_Val
 #To check whether the stack is empty or not
 def isempty(self):
  if self.head == None:
    return True
  else:
    return False
 #Method of printing the stack
 def print(self, temp):
  if temp == self.head and temp!=None:
    self.print(temp.next)
    print(temp.data,end='')
  elif temp:
    self.print(temp.next)
    print(temp.data,end='')
    print(',',end='')
  else:
    return
#object instantiation
st = Stack_structure()
s = StackinArray()
choice=0
while(choice!=3):
 #Getting the choice from the user
 choice = int(input("Enter your choice to perform:\n1 for Stack using Array\n2 for Stack using Linked List\n3 to exit\nYour choice: "))
 #if user enter choice 1 to perform stack on array
 if(choice==1):
  while (True):
    el = int(input("1 for Push\n2 for Pop\n3 To go back to the previous menu\n4 To exit \nYour choice: "))
    if (el == 1):
     element = int(input("Enter Element to push in stack\n"))
     s.push(element)
    elif (el == 2):
     print("The deleted value is :",s.pop())
     print("Stack after popping is",s.stack)
    elif (el==3):
     break
    elif (el==4):
     sys.exit()
    else:
     print("Invalid choice,Please enter a valid choice.")
    #if user enter choice as 2 to perform stack in linked list
 if(choice==2):
   while True:
    ch=int(input("Enter the choice:\n1 for push \n2 for pop \n3 To go back to the previous menu\n4 To exit\nYour choice: "))
    if (ch==1):
     c=int(input("Enter the element u want to push: "))
     st.push_val(c)
     print("[",end='')
     st.print(st.head)
     print("]")
    elif (ch==2):
     del_Val=st.pop_val()
     if del_Val is None:
      print("The stack is empty")
     else:
      print("The deleted value is :",int(del_Val))
      print("The stack after popping is [",end='')
      st.print(st.head)
      print("]\n",end='')
    elif (ch==3):
     break
    elif ch==4:
     sys.exit()
    else:
     print("Invalid choice,Please enter a valid choice.")
    #To exit the program
 if(choice==3):
     sys.exit()
    #To display invalid input
 if(choice>3 or choice<1):
      print("Invalid choice,Please enter a valid choice.")