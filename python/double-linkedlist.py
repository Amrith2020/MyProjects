class Node:
    def __init__(self,val):
        self.item = val
        self.next = None
        self.prev = None

    
class DoublyLinkedList:
    def __init__(self):
        # if there is no node in starting address
        self.start = None

    def insertatend(self, data):
        if self.start is None:
            self.start = Node(data)
        else:
            curr = self.start
            while curr.next is not None:
                curr = curr.next
            # first create a node    [prev|newnode|data|next]
            new_node = Node(data)
            #assign it to the last node [lastnode|next] => [prev|newnode|data|next] => None
            curr.next = new_node
            #reverse connect newnode to current node [lastnode|next] <=> [prev|newnode|data|next] => None
            new_node.prev = curr
            
    def insertatbeg(self, data):
        if self.start is None:
            self.start = Node(data)
        else:
            curr = self.start
            while curr.prev is not None:
                curr = curr.prev
            # first create a node    [prev|newnode|data|next]
            new_node = Node(data)
            #assign it to the first node [prev|newnode|data|next] <=[firstnode|next]
            curr.prev = new_node
            #forward connect newnode to current node [prev|newnode|data|next] <=>[firstnode|next]
            new_node.next = curr

    def insertatpos(self, pos, data):
        if self.start is None:
            self.start = Node(data)
        else:
            curr = self.start
            #navigate to first node
            while curr.prev is not None:
                curr = curr.prev
            
            if pos == 0:
                new_node = Node(data)
                curr.prev = new_node
                new_node.next = curr
                return
            i = 0
            while i < pos:
                i += 1
                curr = curr.next
                if curr is None:
                    print("No valid position {}, if you are trying to enter an element at the last position use the appropriate function".format(pos))
                    return

            new_node = Node(data)
            new_node.next = curr
            temp = curr.prev
            curr.prev = new_node
            new_node.prev = temp
            temp.next = new_node

            



    def deleteatpos(self, pos):
        if self.start is None:
            print("nothin to delete")
        else:
            curr = self.start
            # navigate to first element
            while curr.prev is not None:
                curr = curr.prev

            if pos == 0:
                curr.next.prev = None
                return
            i = 0
            while(i<pos):
                i += 1
                curr = curr.next
                if curr is None:
                    print("No valid element at position {}".format(pos))
                    return

            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def deletebegnode(self):
        if self.start is None:
            print("nothin to delete")
        else:
            curr = self.start
            while curr.prev is not None:
                curr = curr.prev
            #go to next node at begining
            curr = curr.next
            #change the next node prev value to None
            curr.prev = None
            #reset start to the current start (which was the next curr)
            self.start = curr

    def deletelastnode(self):
        if self.start is None:
            print("there is nothing to delete")
        else:
            curr = self.start
            while curr.next is not None:
                curr = curr.next
            curr = curr.prev
            curr.next = None

        while curr.prev is not None:
                curr = curr.prev
        self.start = curr
    
    def printDoubLL(self):
        if self.start == None or (self.start.next is None and self.start.prev is None):
            print("List is empty")
        else:
            curr = self.start
            # go to the beginning
            while curr.prev is not None:
                curr = curr.prev
            print("null<=>",end='')
            #actual printing
            while curr is not None:
                print(curr.item,"<=>", end='')
                curr = curr.next
            print(" null")

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.printDoubLL()
    dll.insertatend(120)
    dll.printDoubLL()
    dll.insertatend(50)
    dll.printDoubLL()
    dll.insertatend(65)
    dll.printDoubLL()
    dll.insertatend(550)
    dll.printDoubLL()
    dll.insertatend(200)
    dll.printDoubLL()
    dll.insertatbeg(330)
    dll.printDoubLL()
    dll.insertatbeg(350)
    dll.printDoubLL()
    dll.insertatbeg(40)
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.insertatbeg(330)
    dll.printDoubLL()
    dll.insertatbeg(350)
    dll.printDoubLL()
    dll.insertatend(50)
    dll.printDoubLL()
    dll.insertatend(65)
    dll.printDoubLL()
    dll.insertatbeg(32)
    dll.printDoubLL()
    dll.insertatend(66)
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.deletebegnode()
    dll.printDoubLL()
    dll.deletebegnode()
    dll.printDoubLL()
    dll.deletebegnode()
    dll.printDoubLL()
    dll.insertatend(77)
    dll.printDoubLL()
    dll.insertatbeg(33)
    dll.printDoubLL()
    dll.deletebegnode()
    dll.printDoubLL()
    dll.deletelastnode()
    dll.printDoubLL()
    dll.insertatend(550)
    dll.printDoubLL()
    dll.insertatend(200)
    dll.printDoubLL()
    dll.insertatbeg(330)
    dll.printDoubLL()
    dll.insertatbeg(350)
    dll.printDoubLL()
    dll.insertatbeg(40)
    dll.printDoubLL()
    dll.deleteatpos(4)
    dll.printDoubLL()
    dll.deleteatpos(0)
    dll.printDoubLL()
    dll.deleteatpos(1)
    dll.printDoubLL()
    dll.deleteatpos(2)
    dll.printDoubLL()
    dll.deleteatpos(10)
    dll.printDoubLL()
    dll.deleteatpos(0)
    dll.printDoubLL()
    dll.insertatend(550)
    dll.printDoubLL()
    dll.insertatend(200)
    dll.printDoubLL()
    dll.insertatbeg(330)
    dll.printDoubLL()
    dll.insertatbeg(350)
    dll.printDoubLL()
    dll.insertatbeg(40)
    dll.printDoubLL()
    dll.insertatpos(3,10)
    dll.printDoubLL()
    dll.insertatpos(0,12)
    dll.printDoubLL()
    dll.insertatpos(10,52)
    dll.printDoubLL()
    

    
    
            





    