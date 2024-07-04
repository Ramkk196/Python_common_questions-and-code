class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list:
    def __init__(self):
        self.head =None
    def insert(self,value):
        position=0
        if self.head is None:
            self.head=Node(value)
            current_node=self.head
            current_node.index=position
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
                position=position+1
            current_node.next=Node(value)
            current_node=current_node.next
            current_node.index=position+1
    def delete (self ):
        current_node=self.head
        while current_node.next.next is not None:
           current_node=current_node.next
        current_node.next=None
        current_node=self.head
        while current_node is not None:
            print(current_node.value,"---->",end="")
            current_node=current_node.next
if __name__ == "__main__":
    new_list=Linked_list()
    new_list.insert(5)
    new_list.insert(7)
    new_list.insert(11)
    new_list.delete()

