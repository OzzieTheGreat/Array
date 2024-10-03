class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
def split(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next
    second = slow.next
    slow.next = None
    return second
def merge(first, second):
    if not first:
        return second
    if not second:
        return first
    if first.data < second.data:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second
def merge_sort(head):
    if not head or not head.next:
        return head
    second = split(head)
    head = merge_sort(head)
    second = merge_sort(second)
    return merge(head, second)
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()
def average(head):
    if(head == None):
        return -1
    count = 0
    sum = 0
    avg = 0.0
    while (head != None):
        count += 1
        sum += head.data
        head = head.next
    avg = sum / count
    return avg
if __name__ == "__main__":
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(7)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next = Node(5)
    print("\nThe Given Unsorted Single Linked List: ")
    print_list(head)
    head = merge_sort(head)
    print("\nThe Sorted Single Linked List in Ascending Order: ")
    print_list(head)
    print("\nThe Average Value of Even Elements in Single Linked List:",average(head))
    average(head)
