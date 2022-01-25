import array


def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

        for i in arr:
            print(i),
        print

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    for i in arr:
        print(i),
    print
    
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
def printArr(arr):
    print
    print("The Array Elements are : ")
    for i in arr:
        print(i),
    print

arr = array.array('I', [])
for i in range(0,15):
    temp = int(input("Enter The Integer Element For Index {} -> ".format(str(i))))
    arr.append(temp)
printArr(arr)
print()
choice = int(input("Enter the choice u want to perform\n1.)Selection sort\n2.)Merge sort\n"))
if choice == 1:
    selectionSort(arr)
    printArr(arr)
elif choice == 2:
    mergeSort(arr, 0, len(arr)-1)
    printArr(arr)
else:
    print("Invalid choice, choose from the given choice.")
