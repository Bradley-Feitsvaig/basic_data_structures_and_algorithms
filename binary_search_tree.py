#Binary search tree Implementation
from misc import *
class Node:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def insert(self,value):
        n = Node(value)
        if self.root is None:
            self.root=n
        else:
            current_node =self.root
            while True:
                if value<current_node.value:
                    #left
                    if current_node.left is None:
                        current_node.left = n
                        return self
                    current_node = current_node.left
                else:
                    #right
                    if current_node.right is None:
                        current_node.right = n
                        return self
                    current_node=current_node.right

    def lookup(self,value):
        if self.root is None:
            return False
        current_node= self.root
        while current_node:
            if value<current_node.value:
                #left
                current_node = current_node.left
            elif value>current_node.value:
                #right
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return False
    
    def remove(self,value):
        pass

    def bfs(self):  #Iterative
        current_node = self.root
        list = []
        queue = []
        queue.append(current_node)

        while(len(queue)>0):
            current_node=queue.pop(0)
            list.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list

    def bfs_recursive(self,list,queue): #Recursive
        if len(queue)==0:
            return list
        current_node = queue.pop(0)
        list.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.bfs_recursive(list,queue)
        

           
def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    tree.insert(10)
    tree.insert(2)
    tree.insert(0)
    displayBinarySearchTree(tree.root)  #Display function for binary tree in misc file

    n = tree.lookup(16)
    if n:
        displayBinarySearchTree(n) #Display the subtree in case it find a node with wanted value
    else:
        print("False")
    
    n = tree.lookup(20)
    if n:
        displayBinarySearchTree(n) #Display the subtree in case it find a node with wanted value
    else:
        print("False")

    print("The tree in BFS order: " + str(tree.bfs()))

    bfs_order = []
    queue_for_bfs_recursive = [tree.root]
    tree.bfs_recursive(bfs_order,queue_for_bfs_recursive)
    print("The tree in BFS_recursive order: " + str(bfs_order))

if __name__ == "__main__":
    main()