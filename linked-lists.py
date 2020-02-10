#Linked lists are composed of nodes and references / pointers pointing from one node to the other
#The last reference is pointing to a NULL
# Each node contains data and a reference to the next node
# Many basic operations such as obtaining the last node of the list or finding a node 
#that contains a given data - require sequential scanning of most or all the list elements.

#Advantages:
    # They are dynamic data structures, arrays are not
    # I can allocate the needed memory in run-time
    # Very efficient if we want to manipulate the first elements
    # Can store items with different sizes
    # Easy to grow organically. An array's size needs to be known ahead of time, or re-created when it needs to grow

#Disadvantages:
    # Waste of memory because of the references
    # Nodes must be read in order from the beginning because linked lists have sequential access
    # Very difficult to navigate backwards, we can use doubly linked lists, but with more memory waste because of the back pointer.

# Operations:
  #Insertion: O(1) time complexity. list.insertAtStart(10);
  #IMPORTANT: arrays are fast for inserting items at the end and linked lists are fast for inserting at the beginning.
  #Removing: list.removeStart(). It is very fast

# How to choose between array and lined list?
        #Array if we want random indexing access and modify the end of the list
        #Lined list if we want to modify the beginning of the list
        #Search: is better use arrays  IF WE KNOW THE INDEX because of the index based system. A linked list would be too slow, it requires the traversal through all the items for searching and element.
        #Insert at the start: better use linked lists.
        #Insert at the end: is better use arrays.
        #Deletion: is better use a linked list. Deletion only requires change in the pointer location.
        #Memory managemen: is better an array, because linked lists need extra memory because of the pointers.

#Very nice implementation: https://github.com/kojino/data-structures-algorithms/tree/master/linked_list
#Node class. Inplement a linked list:

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None #The pointer initially points to nothing

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

node1.traverse()

#Traversing values:

class Node:
    ...
    def traverse(self):
        node = self #start from the head node
        while node != None:
            print node.val #access the node value
            node = node.next #move on to the next node
            
     node1.traverse()
            
#Doubly linked list

class DoublyNode:
    def __init__(self, val):
        self.val = data
        self.next = None
        self.pre = None

        
#insert

class Node(object):
    def __init__(self, data):
        sel.data = data;
        self.nextNode = None;

class LinkedList(object):
    def __init__(self):
        self.head = None;
        self.size = 0;

def insertStart(self, data):
    self.size = self.size + 1;
    newNode = Node(data);

    if not self.head:
        self.head = newNode;
    else:
        newNode.nextNode = self.head;
        self.head = newNode;

#O(1), constant time complexity
def size(self):
    return self.size;

#O(N), linear time complexity
def size2(self):
    actualNode = self.head;
    size = 0;

    while actualNode is not None:
        size += 1;
        actualNode = actualNode.nextNode;

    return size;
