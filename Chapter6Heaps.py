def InputFunction():
    arr = []
    n = int(input("Enter a number of elements in the array: "))
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        arr.append(element)
    return arr

def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

arr = InputFunction()
heapSort(arr)
print("Sorted array in decreasing order:")
printArray(arr)
