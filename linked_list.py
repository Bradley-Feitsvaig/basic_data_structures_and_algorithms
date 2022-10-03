#Linked Lists Implementation

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,node):
        if self.head ==None:
            self.head = node
        if self.tail==None:
            self.tail = node
        else:
            node.prev=self.tail
            self.tail.next=node
        self.tail=node
        self.length+=1

    def prepend(self,node):
        if self.tail == None:
            self.tail = node
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length+=1

    def insert(self,node,index):
        if index> self.length or index<0:
            return "Cant"
        elif index ==0:
            self.prepend(node)
        elif index ==self.length:
            self.append(node)
        else:
            i=0
            temp = self.head
            while i<index-1:
                 temp = temp.next
                 i+=1
            node.prev=temp
            node.next = temp.next
            temp.next=node
            node.next.prev=node
            self.length +=1
    
    def remove(self,index):
        if index <= 0:
            self.head = self.head.next
            self.head.prev=None
            self.length -=1
            return
        if index>=self.length:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            self.tail=temp
            self.length -=1
            return
        temp = self.head
        i=0
        while i<index-1:
            temp = temp.next
            i+=1
        temp.next.prev=temp.prev
        temp.next=temp.next.next
        self.length -=1

    def __str__(self) -> str:
        temp = self.head
        s='Length : ' + str(self.length) + '\n'
        while temp!=None:
            s+= str(temp.value) + '--->'
            temp = temp.next

        return s

class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
        self.prev=None
    def __str__(self) -> str:
        return str(self.value)




def main():
    l=LinkedList()
    for i in range(5):
        l.append(Node(i))
    l.prepend(Node(123))
    l.prepend(Node(13))
    l.insert(Node(999),4)
    print(l)
    l.remove(2)
    print(l)
    l.remove(50)
    print(l)
    l.remove(5)
    print(l)
    l.remove(0)
    print(l)

if __name__ == "__main__":
    main()