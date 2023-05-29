#singly and doubly linked list implementation and their operations


class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev



class SinglyLinkedList:
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
    

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return

        temp=self.head
        msg=True
        while temp:
            if temp.data == data_after:
                node=Node(data_to_insert,temp.next)
                temp.next=node
                msg=False
                break
                
            temp=temp.next
        if msg == True:
            raise Exception('invalid value')
        
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head=self.head.next    
            return
        
        temp=self.head
        while temp.next:
            if temp.next.data == data:
                temp.next=temp.next.next
                break
            temp=temp.next
    
            
    
            
class DoublyLinkedList:

    def __init__(self) :
        self.head=None

    def add_beginning(self,data):
        if self.head is None:
            node=Node(data,None,None)
            self.head=node
            
        else:
            node =Node(data,self.head,None)
            self.head.prev=node
            self.head=node
    def add_end(self,data):
        if self.head is None:
            node=Node(data,None,None)
            self.head=node
            return

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None,temp)

    def get_lastnode(self):
        if self.head is None:
            return self.displayNode()
        if self.head.next == None:
            return self.head.data

        temp=self.head
        while temp.next:
            temp=temp.next
        return temp
    def getLength(self):
        if self.head is None:
            return
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def removeIndexItem(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("invalid index")
        
        if index == 0:
            self.head=self.head.next
            self.head.prev=None
            return

        count=0
        temp=self.head
        while temp:
            if count==index:
                temp.prev.next=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
                    break
                    
                
            temp=temp.next
            count+=1    
    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head=self.head.next
            self.head.prev=None
            return

        temp=self.head
        msg=True
        while temp:
            if temp.data == data:
                temp.prev.next=temp.next
                msg=False
                if temp.next:
                    temp.next.prev=temp.prev
                    break
            temp=temp.next
        if msg == True:
            raise Exception('invalid value')
    
    def insertAtIndex(self,index,data):
        if self.head is None:
            return
        if index<0 or index>=self.getLength():
            raise Exception("invalid index")
        
        if index == 0:
            node=Node(data,self.head,None)
            self.add_beginning(data)
            return

        temp=self.head
        count=0
        while temp:
            if count == index-1:
                node=Node(data,temp.next,temp)
                if node.next:
                    node.next.prev=node
                temp.next=node

            count+=1
            temp=temp.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return


        if self.head.data == data_after:
            temp=self.head
            node=Node(data_to_insert,temp.next,temp)
            temp.next=node
            temp.next.prev=node
            return
        temp=self.head
        while temp:
            if temp.data == data_after:
                node=Node(data_to_insert,temp.next,temp)
                temp.next=node
                if node.next:
                    node.next.prev=node
            temp=temp.next
            
            
        


        
        
        
    def backward(self):
        if self.head is None:
            return
        
        lst=self.get_lastnode()
        temp=lst
        blst=''
        while temp:
            blst+=str(temp.data)
            temp=temp.prev
            if temp:
                blst+='==>'
        print(blst)

    def forward(self):
        if self.head is None:
            return
        
        temp=self.head
        flst=''
        while temp:
            flst+=str(temp.data)
            temp=temp.next
            if temp:
                flst+='==>'
        print(flst)

            

        

    def displayNode(self):
        if self.head is None:
            print('linked list is empty')
            return

        temp=self.head
        dlst=''
        while temp:
            dlst+=str(temp.data)
            temp=temp.next
            if temp:
                dlst+='==>'
            
        print(dlst)
        
            
        


if __name__ == "__main__":
    # obj=SinglyLinkedList()
    # obj.insertEnd(1)
    # obj.insertEnd(2)
    # obj.insertEnd(3)
    # obj.insertEnd(4)
    # obj.remove_item(3)
    # obj.displayNode()
    obj=DoublyLinkedList()
    obj.add_end(1)
    obj.add_end(2)
    obj.add_end(3)
    obj.add_end(4)
    obj.add_end(5)
    obj.insert_after_value(4,22)
    # obj.remove_by_value(5)
    obj.insertAtIndex(4,111)

    obj.backward()
    # obj.forward()
    obj.displayNode()
    
    