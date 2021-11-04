# Convertendo uma lista ligada numa lista circular
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.link_type = "linked"
    
    
    def append(self, _new_data):
        new_node = Node(_new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        
        while(last.next):
            last = last.next
        
        last.next = new_node
    

    def print_list(self):
        if self.head is None:
            print("Vazio... Igualzinho tua cabeça!!!")
            return
        
        temp = self.head
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " -> "
            temp = temp.next
        
        print(list_data)
    
    def print_circular(self):
        if self.head is None:
            print("Vazio... Igualzinho tua cabeça!!!")
            return
        
        temp = self.head
        list_data = ""
        
        while True:
            list_data += str(temp.data) + " -> "
            temp = temp.next
            
            if temp == self.head:
                break
        
        list_data += str(temp.data) + " ->..."
        print(list_data)
    
    
    def print_self(self):
        switch = {
            "linked" : self.print_list,
            "circular" : self.print_circular
        }
        
        switch[self.link_type]()
    
    
    def convert_to_circular(self):
        self.link_type = "circular"
        temp = self.head
        
        if self.head is None or self.head.next is None:
            return
        
        while temp:
            if temp.next is None:
                temp.next = self.head
                return
            
            temp = temp.next
    
    
    def convert_to_list(self):
        self.link_type = "linked"
        temp = self.head
        
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = None


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_self()

list1.convert_to_circular()
list1.print_self()

list1.convert_to_list()
list1.print_self()
