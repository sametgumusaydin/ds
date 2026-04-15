class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LList:
    def __init__(self):
        self.head=None
    def add_front(self,data):
        new =Node(data)
        if self.head is Node:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def add_end(self,data):
        new=Node(data)
        tmp = self.head
        if self.head is None:
            self.head=new
        else:
            while tmp.next is not None:
                tmp=tmp.next
            tmp.next=new

    def delete(self,data):
        tmp=self.head
        if self.head.data==data:
            self.head=self.head.next
        else:
            prev = self.head
            while tmp.next is not None:
                prev=tmp
                tmp=tmp.next
                if tmp.data==data:
                    prev.next=tmp.next
    def count(self):
        if self.head ==None:
            print('zero is hero')
        else:
            counter=1
            tmp=self.head
            while tmp.next !=None:
                counter+=1
                tmp=tmp.next
            print(counter)


    def display(self):
        tmp=self.head
        while tmp is not  None:
            print(tmp.data, "-->", end=" ")
            tmp =tmp.next




import random
A=LList()
arr=[]
for i in range(6):
    r=random.randint(1,20)
    print(r)
    arr.append(r)
    if r<10:
        A.add_front(r)
    else:
        A.add_end(r)
A.display()
print('_______')
print(arr)
#????????????????????? is it ............... ???
