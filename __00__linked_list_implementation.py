'''
    LinkedList() will initialize an empty linked list.

    int get(int i)
        will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.

    void insertHead(int val)
        will insert a node with val at the head of the list.

    void insertTail(int val)
        will insert a node with val at the tail of the list.

    int remove(int i)
        will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.

    int[] getValues()
        return an array of all the values in the linked list, ordered from head to tail.
'''

class ListNode:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_head(self,data):
        new_node = ListNode(data)

        new_node.next = self.head
        self.head = new_node

        #if list was empty, make tail same as head
        if not new_node.next:
            self.tail = new_node

    def insert_at_tail(self,data):
        new_node = ListNode(data)

        #if tail not empty
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            #if tail empty, means list is empty, so make both head and tail point to the new node
            self.head = new_node
            self.tail = new_node

    def remove(self,i):
        current = self.head
        count = 0

        #remove the 0-th node
        if i == 0:
            #if head is the only node,
            if not current.next:
                self.head = None
                self.tail = None
            else:
                #if there are other nodes besides head, just move the head to the next node
                self.head = current.next

        #the current pointer should stop before the i-th node
        while current and count < i - 1:
            count += 1
            current = current.next

        #delete in the middle, also check if last node is being deleted
        if current and current.next:
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next
            return True

        return False

    def getValues(self):
        values = []

        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return values

    #implemented just for testing other functions regarding linked lists
    def getHead(self):
        return self.head

    #implemented just for testing other functions regarding linked lists
    def getValuesFromHead(self,head):
        values = []
        current = head
        while current:
            values.append(current.data)
            current = current.next

        return values