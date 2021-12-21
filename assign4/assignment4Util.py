from assignment4Structure import *
import random
def sort1(ll):
    #selection sort
    swapped = True
    storage = []
    node = ll.head
    while node is not None:
        if type(node.cargo) == type(LinkedList()):
            list1 = convertList((node.cargo))
            storage.append(list1)
            node = node.next
        else:
            storage.append(node.cargo)
            node = node.next

# check for case with a linked list inside of the cargo
    for i in range(len(storage)):
        minIndex = i
        for j in range(i,len(storage)):
            #print("type storage[j]", type(storage[j]), ", type storage[minIndex]", type(storage[minIndex]))
            if type(storage[j]) == type([]) and type(storage[minIndex]) != type([]):
                if storage[j][0] < storage[minIndex]:
                    minIndex = j
            if type(storage[minIndex]) == type([]) and type(storage[j]) != type([]):
                if storage[j] < storage[minIndex][0]:
                    minIndex = j
            if type(storage[j]) != type([]) and type(storage[minIndex]) != type([]):
                if storage[j] < storage[minIndex]:
                    minIndex = j
            if type(storage[j]) == type([]) and type(storage[minIndex]) == type([]):
                if storage[j][0] < storage[minIndex][0]:
                    minIndex = j


        storage[minIndex],storage[i] = storage[i],storage[minIndex]

    sorted = LinkedList()
    print(storage)
    # convert back to linked list
    for i in range(len(storage)):
        if type(storage[i]) == type([]):
            LL2 = LinkedList()
            for x in range(len(storage[i])):
                LL2.insert(storage[i][x])
            sorted.insert(LL2)

        else:
            sorted.insert(storage[i])

    return sorted

def convertList(ll):
    node = ll.head
    list = []
    x = ll.size()
    for i in range(x):
        list.append(node.cargo)
        node = node.next

    return list

def sort2(ll):
    #merge sort

    storage = []
    node = ll.head
    while node is not None:

        storage.append(node.cargo)
        node = node.next
    # the merge sort
    def merge(list):

        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            merge(left)
            merge(right)

            x = 0
            y = 0
            z = 0
            while x < len(left) and y < len(right):
                if left[x] < right[y]:
                    list[z] = left[x]
                    x += 1
                else:
                    list[z] = right[y]
                    y += 1
                z += 1

            while x < len(left):
                list[z] = left[x]
                x += 1
                z += 1

            while y < len(right):
                list[z] = right[y]
                y += 1
                z += 1
        return (list)
    sorted = merge(storage)
    print(sorted)
    sortedLL = LinkedList()
    for i in range(len(sorted)):
        sortedLL.insert(sorted[i])
    return sortedLL

def sumList(ll):
    #basically the size function except you add up all the cargo instead of the number of cargo
    node = ll.head
    sum = 0
    while node is not None:
        if type(node.cargo) == type(LinkedList()):
            hold =convertList(node.cargo)
            sum = sum + hold[0]
            # too call a function you have treat the function like an attribute^
            # not like this: size(node.cargo)
            node = node.next
        else:
            sum = sum + node.cargo
            node = node.next

    return sum
    # still needs to be changed just copied the size function over

def printAll(ll):
    node= ll.head
    while node is not None:
       if type(node.cargo) == type(LinkedList()):
            printAll(node.cargo)
            node = node.next
       else:
         print(str(node.cargo))
         node = node.next

def shuffle(ll):
    list = convertList(ll)
    print(list)
    x = random.randint(1,len(list))
    for i in range(len(list)-1):
        list[i],list[x] = list[x],list[i]
    print(list)
    linked = LinkedList()
    for i in list:
        linked.insert(i)
    return linked



if __name__ == "__main__":

    import random

    # Test 1
    ll = LinkedList()
    _sum = 0

    for x in range(10):
        rNum = random.randint(1, 100)
        _sum += rNum
        ll.insert(rNum)
    assert not ll.isEmpty()
    assert ll.size() == 10
    print("Pre-sort Linked List:\n")
    printAll(ll)
    sortedLL = sort1(ll)
    assert not sortedLL.isEmpty()
    assert sortedLL.size() == 10
    assert sumList(sortedLL) == _sum
    print("Post-sort Linked List:\n")
    printAll(sortedLL)

    # Test 2

    ll = LinkedList()

    for x in range(10):
        ll.insert(random.randint(1, 100))
    assert not ll.isEmpty()
    assert ll.size() == 10
    print("Pre-sort Linked List:\n")
    printAll(ll)
    sortedLL = sort2(ll)
    assert not sortedLL.isEmpty()
    assert sortedLL.size() == 10
    print("Post-sort Linked List:\n")
    printAll(sortedLL)

    # Test 3
    ll = LinkedList()
    _sum = 0
    for x in range(10):
        rNum = random.randint(1, 100)
        _sum += rNum
        if x % 3 == 0 and x != 0:
            subLL = LinkedList()
            for y in range(x):
                subLL.insert(rNum)
            ll.insert(subLL)
        else:
            ll.insert(rNum)
    assert not ll.isEmpty()
    assert ll.size() == 25
    print("Pre-sort Linked List:\n")
    printAll(ll)
    sortedLL = sort1(ll)
    assert not sortedLL.isEmpty()
    assert sortedLL.size() == 25
    assert sumList(sortedLL) == _sum
    print("Post-sort Linked List:\n")
    printAll(sortedLL)

# testing the shuffle
# does this count for my unit test?
    #please??
    print("Hey check out my shuffle function")
    ll = LinkedList()
    _sum = 0

    for x in range(10):
        rNum = random.randint(1, 100)
        _sum += rNum
        ll.insert(rNum)
    assert not ll.isEmpty()
    assert ll.size() == 10
    print("Pre-sort Linked List:\n")
    printAll(ll)
    sortedLL = shuffle(ll)
    assert not sortedLL.isEmpty()
    assert sortedLL.size() == 10
    assert sumList(sortedLL) == _sum
    print("Post-sort Linked List:\n")
    printAll(sortedLL)
