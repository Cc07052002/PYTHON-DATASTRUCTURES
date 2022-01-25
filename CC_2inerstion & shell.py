import array

def insertionSort(arr):
    print(list(arr))
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(list(arr))

def shellSort(arr):
    print(list(arr))
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
            print(list(arr))
        gap //= 2

tempA = list(eval(input("Enter the 15 integer elements in a comma seperated way - > ")))
ar = array.array('I',tempA)
print('The Elements In Array Brfore Sorting - >')
for i in ar:
    print(i, end=' ')
print()
print('Enter The Number Of Your Choice:\n\t1] Insertion Sort \n\t2] Shell Sort.')
choice = int(input("Your Choice -> "))
print()
if choice == 1:
    insertionSort(ar)
elif choice == 2:
    shellSort(ar)
else:
    print("Choose From The Given Option.")
    choice = int(input("Your Choice -> "))

