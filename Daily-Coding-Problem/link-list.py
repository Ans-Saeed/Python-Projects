# This is the implementation of singly linked list. 
class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class link_list:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node= Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node

    def print_list(self):
        current_node=self.head
        while current_node is not None:
            print (current_node.data, end=" ")
            current_node=current_node.next
            print()


def mergeTwoLists(list1,list2):
    
    pass

# Create a new linked list
my_list = link_list()

# Add some nodes to the list
my_list.add_node(12)
my_list.add_node(21)
my_list.add_node(36)

# Print the contents of the list
my_list.print_list()