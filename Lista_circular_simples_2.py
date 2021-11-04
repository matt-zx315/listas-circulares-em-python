# Ordenando uma lista circular
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
                    self.add_to_end(_data)
                    return
                
                new_node.next = temp.next
                temp.next = new_node
                return
            
            temp = temp.next
    
    
    def add_ordered(self, _data):
        # Caso 1: Lista vazia
        if self.last is None:
            self.add_to_empty(_data)
            return
        # Caso 2: Lista com apenas um nó
        elif self.last.next == self.last:
            # 2.1: Dado inserido menor que dado existente
            if _data <= self.last.data:
                self.add_to_front(_data)
                return
            # 2.2: Dado inserido maior que dado existente
            else:
                self.add_to_end(_data)
                return
        # Caso 3: Lista com dois ou mais nós
        else:
            # 3.1: Dado inserido menor que o menor valor existente
            if _data <= self.last.next.data:
                self.add_to_front(_data)
                return
            # 3.2: Dado inserido maior que o maior valor existente
            elif _data > self.last.data:
                self.add_to_end(_data)
                return
            # 3.3: Dado inserido entre o maior e o menor
            else:
                aux = self.last
                
                while _data > aux.next.data:
                    aux = aux.next
                
                self.add_after(_data, aux.data)
                return
    
    
    def sort_list(self):
        sorted_list = Circular_List()
        
        aux = self.last.next
        visited = set()
        
        while aux.data not in visited:
            sorted_list.add_ordered(aux.data)
            visited.add(aux.data)
            aux = aux.next
        
        return sorted_list
    
    
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
list1.add_to_end(72)
list1.add_to_end(64)
list1.add_to_end(17)
list1.add_to_end(89)
list1.add_to_end(35)
list1.add_to_end(96)
list1.add_to_end(51)
list1.print_list()

list1 = list1.sort_list()
list1.print_list()

# list1.add_ordered(72)
# list1.print_list()

# list1.add_ordered(64)
# list1.print_list()

# list1.add_ordered(17)
# list1.print_list()

# list1.add_ordered(89)
# list1.print_list()

# list1.add_ordered(35)
# list1.print_list()

# list1.add_ordered(96)
# list1.print_list()

# list1.add_ordered(51)
# list1.print_list()
