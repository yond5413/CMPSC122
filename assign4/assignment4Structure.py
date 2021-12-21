class Node():
    def __init__(self,cargo = None,next = None):
        self.cargo = cargo
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,value):
        Newnode = Node(value)
        node = self.head

        if node is None:
            self.head = Newnode
            return

        while node.next is not None:
            node = node.next

        node.next = Newnode

    def size(self):
        node = self.head
        #check if each is not none
        #check each type (None,LinkedList,Int)
        #if type is a linked list recursive
        sum = 0
        while node is not None:
            if type(node.cargo) == type(LinkedList()):
                sum = sum + node.cargo.size()
                # too call a function you have treat the function like an attribute^
                # not like this: size(node.cargo)
                node = node.next
            else:
                node = node.next
                sum+=1

        return sum

    def isEmpty(self):
        return self.head is None


    # change the printall from the one seth gave
