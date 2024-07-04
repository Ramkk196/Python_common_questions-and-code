class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            current_node=self.head
            while current_node.next is  not None :
                current_node=current_node.next
            current_node.next=Node(value)
    def search_list(self,value):
        position=1
        current_node=self.head

        while current_node is not None:
            if current_node.value==value:
                print("found at position")
                print(position)
                return

            else:
                current_node=current_node.next
                position=position+1

        print("no element as such is present ")
    def print_list(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.value,"---->",end="")
            current_node=current_node.next

if __name__ =="__main__"   :
    sample_list = Linked_list()
    while True:
        case = int(input("for insert type 1 in the console for search type 2 and 3 for print"))
        if (case == 1):

            n = int(input("enter the number of elements"))

            for i in range(0, n):
                sample_list.insert(input())
            sample_list.print_list()
        if (case == 2):
            element = input("enter the element to be searched")
            sample_list.search_list(element)
        if (case == 3):
            sample_list.print_list()







