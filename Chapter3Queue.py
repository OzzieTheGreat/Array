def get_input():
    list = []
    n = int(input("Enter a number of elements: "))
    for i in range(0,n):
        element = int(input())
        list.append(element)
    return list
def queReverse(q):
    if (len(q)==0):
        return
    fr = q[0]
    q.pop(0)
    queReverse(q)
    q.append(fr)
mylist = get_input()
print(mylist)
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
queReverse(queue)
print(queue)