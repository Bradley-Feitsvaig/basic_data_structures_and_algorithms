#Stack Implementation (with Linked Lists)

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next=None
    
class Stack:
    def __init__(self) -> None:
        self.top=None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return str(self.top.value) + " On top"

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            self.length-=1
            value = self.top.value
            self.top=self.top.next
            if self.is_empty():
                self.bottom=None
            return str(value) + " popped"


    def push(self,value):
        n = Node(value)
        if self.is_empty():
            self.top=n
            self.bottom=n
        else:
            n.next=self.top
            self.top=n
        self.length+=1

    def is_empty(self):
        return self.length==0

    def __str__(self) -> str:
        temp = self.top
        s = "Length :" + str(self.length)+'\n'
        while temp:
            s+= "|"+str(temp.value) + '|\n' + '|--|' + '\n'
            temp=temp.next
        return s



def main():
    s = Stack()
    s.push(12)
    print(s)
    s.push("ok")
    print(s)
    s.push(15)
    print(s)
    s.push(17)
    print(s)
    print(str(s.pop()))
    print(s)
    print(str(s.peek()))
    print(s)
    print(str(s.pop()))
    print(s)

if __name__ == "__main__":
    main()
