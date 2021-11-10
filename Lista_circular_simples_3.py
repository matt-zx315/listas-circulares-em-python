# Invertendo uma lista circular
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None
    
    
class Circular_List:
    
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def insert_end(self, _data):
        node = Node(_data)
        
        if self.head is None:
            self.head = node
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
    
    
    def print_list(self):
        aux = self.head
        list_info = ""
        
        while self.head:
            list_info += f'{aux.data} -> '
            aux = aux.next
            
            if aux == self.head:
                list_info += '...\n'
                print(list_info)
                return
        
        print("Vazio... Igual sua alma.")
        return
    
    
    def reverse_list(self):
        prev, curr, last = self.tail, self.head, self.head
        
        next = curr.next
        print(f'{curr.data} -> {curr.next.data}')
        curr.next = prev
        print(f'{curr.next.data} <- {curr.data}\n')
        prev = curr
        print(f'Nó anterior: {prev.data}')
        curr = next
        print(f'Nó atual: {curr.data}')
        print(f'Próximo nó: {curr.next.data}\n')
        
        while curr != last:
            next = curr.next
            print(f'{curr.data} -> {curr.next.data}')
            curr.next = prev
            print(f'{curr.next.data} <- {curr.data}\n')
            prev = curr
            print(f'Nó anterior: {prev.data}')
            curr = next
            print(f'Nó atual: {curr.data}')
            print(f'Próximo nó: {curr.next.data}\n')
        
        self.tail = curr
        self.head = prev
        print(f'{self.head.data} <- {self.tail.data}\n')


list1 = Circular_List()
list1.insert_end(72)
list1.insert_end(64)
list1.insert_end(17)
list1.insert_end(89)
list1.insert_end(35)
list1.insert_end(96)
list1.insert_end(51)
list1.print_list()

list1.reverse_list()
list1.print_list()
