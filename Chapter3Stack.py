def reverseArray(arr, n):
    stack = []
    for i in range(n):
        stack.append(arr[i])
    i = 0
    while(len(stack)>0):
        top = stack.pop()
        arr[i] = top
        i += 1
    for i in range(n):
        print(arr[i],end=" ")
n = 5
arr = [10,20,30,40,50]
reverseArray(arr,n)
