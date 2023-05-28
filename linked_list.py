class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class SLinkedList:
    def __init__(self):
        self.head=None

    def insertBeginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def insertEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)

    def displayNode(self):
        if self.head is None:
            print("lisked list is empty")
            return
        temp=self.head
        llst=""
        while temp:
            llst+=str(temp.data)
            temp=temp.next
            if temp:
                llst+='==>'
        print(llst)

    #add set of values to linked list
    def values_list(self,value_list):
        self.head=None
        for data in value_list:
            self.insertEnd(data)


    #get the length of the linked list
    def get_length(self):
        temp=self.head
        count=0
        while temp:
            temp=temp.next
            count+=1

        return count



    def remove_item(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head=self.head.next
            return

        count=0
        temp=self.head
        while temp:
            if count==index-1:
                temp.next=temp.next.next
                break
            temp=temp.next
            count+=1

    def insertAtIndex(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.insertBeginning(data)
            return
        temp=self.head
        count=0
        while temp:
            if count == index-1:
                node=Node(data,temp.next)
                temp.next=node
                break

            count+=1
            temp=temp.next
        



if __name__ == "__main__":
    obj=SLinkedList()
    obj.insertEnd(45)
    obj.insertEnd(46)
    obj.insertEnd(47)
    obj.insertAtIndex(2,3333)
    obj.displayNode()
    print(obj.get_length())