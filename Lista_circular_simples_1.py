# Criando e inserindo elementos em uma lista circular simples
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None
    
    
class Circular_List:
    
    
    def __init__(self):
        self.last = None
    
    def add_to_empty(self, _data):
        if self.last != None:
            self.print_list()
            return
        
        new_node = Node(_data)
        self.last = new_node
        self.last.next = self.last
        return self.last
    
    
    def add_to_front(self, _data):
        if self.last == None:
            self.add_to_empty(_data)
            return
        
        new_node = Node(_data)
        new_node.next = self.last.next
        self.last.next = new_node
    
    
    def add_to_end(self, _data):
        if self.last is None:
            self.add_to_empty(_data)
            return
        
        new_node = Node(_data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
    
    
    def add_after(self, _data, _item):
        if self.last == None:
            self.add_to_empty(_data)
            return
        
        temp = self.last
        new_node = Node(_data)
        
        while temp:
            if temp.data == _item:
                if temp == self.last:
                    self.add_to_end()
                    return
                
                new_node.next = temp.next
                temp.next = new_node
                return
            
            temp = temp.next
    
    
    def print_list(self):
        list_data = ""
        
        if self.last is None:
            print("Vazio igual tua alma...")
            return
        elif self.last.next == self.last:
            list_data += str(self.last.data) + "->..."
            print(list_data)
            return
        else:
            aux = self.last.next
            while aux != self.last:
                list_data += str(aux.data) + " -> "
                aux = aux.next
            
            list_data += str(aux.data) + " -> ..."
            print(list_data)
        

list1 = Circular_List()
list1.print_list()

list1.add_to_empty(89)
list1.print_list()
list1.add_to_empty(64)

list1.add_to_front(64)
list1.print_list()

list1.add_to_end(35)
list1.print_list()

list1.add_to_front(72)
list1.print_list()

list1.add_to_end(96)
list1.print_list()

list1.add_after(17, 64)
list1.print_list()
