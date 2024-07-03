#basic operation of insertion and acessing linked list
lass node:
    def __init__( self,value):
        self.value=value
        self.next=None
class linked_list:
    def __init__(self):
        self.front=None
    def insert (self,value):
        if self.front is None:
             self.front=node(value)
        else:
               item=self.front
               while item.next is not None:
                   item = item.next
               item.next = node(value)
    def acess_list(self,value):

        Front=self.front
        if Front.value == value:
            print("item foind at starting of linked list at position 1 the front end")
        else:

         new_item=self.front
         count=1
         while new_item.next is not None:

            new_item= new_item.next
            count=count+1
            if new_item.value == value:
                print("item found at postion")
                print(count)
                return
            print("no item as such")
         if new_item.value==value:
              print("item found at ")
              print(count)
              print("position")

new_linked_list=linked_list()
new_linked_list.insert(5)
new_linked_list.insert(6)
new_linked_list.insert(7)
new_linked_list.acess_list(6)






