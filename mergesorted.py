import sys, time
from collections import deque

# class LinkedList:
#     def __init__(self, head = None, count = 0):
#         self.head = head
#         self.count = count
    
#     def __str__(self):
#         if(self.data):
#             curr = self
#             out = 'List: ' + curr.data
#             while(curr.next is not None):
#                 curr = curr.next
#                 out = out + ' ' + curr.data
#             return out

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        if(self.data):
            curr = self
            out = 'List:'

            if (curr.data):
                out = out + ' ' + curr.data

            while(curr.next is not None):
                curr = curr.next
                if (curr.data):
                    out = out + ' ' + curr.data
            return out
        return ''

def merge_sorted(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1
    elif head1.data < head2.data:
        new=LinkedListNode(head1.data)
        head1 = head1.next
    else:
        new=LinkedListNode(head2.data)
        head2 = head2.next

    while ((head1 is not None and head1.data) or (head2 is not None and head2.data)):
        print(f'new: {new} head1: {head1}, head2: {head2}')
        if head2 is None or (head1 is not None and int(head1.data) < int(head2.data)):
            curr = new
            new = LinkedListNode(head1.data)
            new.next = curr
            head1 = head1.next
        elif head1 is None or (head2 is not None and int(head2.data) < int(head1.data)):
            curr = new
            new = LinkedListNode(head2.data)
            new.next = curr
            head2 = head2.next
    while (new.next is not )
    return new

def merge_sorted_deque(head1, head2):
    head1 = deque(head1)
    head2 = deque(head2)

    index = 0
    while (head2):
        print(index, head1[index], head2[0], head1, head2)
        if not head2[0].isdigit():
            head2.popleft()
        elif not head1[index].isdigit() and head2[0].isdigit():
            head1.insert(index,head2.popleft())
        elif int(head1[index]) > int(head2[0]):
            head1.insert(index,head2.popleft())
        index= index + 1

    return head1

def main() -> int:
    first_inlist = sys.argv[1].split(',')
    second_inlist = sys.argv[2].split(',')

    # fllist = LinkedList()
    temp1 = LinkedListNode(first_inlist[-1])
    # fllist.head = temp
    # fllist.count = fllist.count + 1
    
    for x in range(1,len(first_inlist)):
        curr = temp1
        temp1 = LinkedListNode(first_inlist[::-1][x])
        temp1.next = curr
    # print(temp1.next)
    print(temp1)
    
    temp2 = LinkedListNode(second_inlist[-1])
    # sllist.head = temp
    # sllist.count = sllist.count + 1
    
    for x in range(1,len(second_inlist)):
        curr = temp2
        temp2 = LinkedListNode(second_inlist[::-1][x])
        temp2.next = curr
        # sllist.count = sllist.count + 1
    print(temp2)


    start = time.time()
    complex_func = merge_sorted_deque(first_inlist, second_inlist)
    end = time.time()

    print(f"merge_sorted_deque ouputs: {complex_func} with time of {end-start}")

    start = time.time()
    complex_func = merge_sorted(temp1, temp2)
    end = time.time()

    print(f"merge_sorted ouputs: {complex_func} with time of {end-start}")

    return 0

if __name__ == '__main__':
    sys.exit(main())