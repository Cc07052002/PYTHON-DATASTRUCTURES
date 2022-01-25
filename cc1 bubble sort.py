def bubbleSort():
    n = len(arr)
    for i in range(n):#let the length of the arr be 5
        for j in range(0, n-i-1):#The right most element would be sorted after the 1st iteration(0,5-0-1)
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insert():
    element = int(input("Enter the integer element to be inserted -> "))
    arr.append(element)
    print()
    
def delete():
    element = int(input("Enter the integer element to be deleted -> "))
    if element in arr:
        arr.remove(element)
    else:
        print(str(element) + " is not found in the Array.")
    print()
    
def printArr():
    print("The elements in the array are : ")
    for i in arr:
        print(i, end = ' ')
    print('\n')
    
arr = []

print("Enter the number of your choice : \n\t1] Insert\n\t2] Delete\n\t3] Print\n\t4] Bubble Sort\n\t5] Exit")

while True:
    choice = int(input("Enter the number of your choice :"))
    
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        printArr()
    elif choice == 4:
        print("The array before bubble sorting is ")
        printArr()
        bubbleSort()
        print("The array after bubble sorting is ")
        printArr()
        break
    elif choice == 5:
        break
    else:
        print("The choice is not found in the range of (1-4).")
        print()
