#Queue Implementation (with Doubly Linked List)

from faulthandler import is_enabled
from tkinter import N
from xmlrpc.client import Boolean


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self) -> str:
        if self.is_empty():
            return "Queue is empty"
        else:
            return str(self.last.value) + " is first in the Queue"

    def dequeue(self) -> str:
        if self.is_empty():
            return "Queue is empty"
        value = self.last.value
        if self.length == 1:
            self.first = None #first node of the linked list (last in the queue)
            self.last = None  #last node of the linked list (first in the queue)
        else:
            self.last = self.last.prev
            self.last.next = None
        self.length-=1
        return "Dequeued "+str(value)

    def enqueue(self,value) -> str:
        n = Node(value)
        if self.is_empty():
            self.first = n
            self.last = n
            self.length+=1
            return "Enqueued "+str(value)
        else:
            self.first.prev = n
            n.next=self.first
            self.first=n
            self.length+=1
            return "Enqueued "+str(value)


    def is_empty(self) -> bool:
        return self.length == 0

    def __str__(self) -> str:
        s = "Queue: length " +str(self.length)+'\n'
        temp = self.first
        while temp:
            s+= str(temp.value)+"==>"
            temp=temp.next
        return s

def main():
    q = Queue()
    print(q.enqueue("Google"))
    print(q)
    print(q.enqueue(123))
    print(q)
    print(q.enqueue("Amazon"))
    print(q)
    print(q.enqueue("GitHub"))
    print(q)
    print(q.peek())
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)

if __name__ == "__main__":
    main()