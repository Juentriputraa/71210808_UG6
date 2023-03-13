class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.current_node = None
    
    def addElementHead(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.next_node = self.head_node
            self.head_node.prev_node = new_node
            self.head_node = new_node
        self.current_node = self.head_node
    
    def addElementTail(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.prev_node = self.tail_node
            self.tail_node.next_node = new_node
            self.tail_node = new_node
        self.current_node = self.head_node
    
    def maju(self, steps):
        for i in range(steps):
            if self.current_node.next_node is not None:
                self.current_node = self.current_node.next_node
            else:
                break
        return self.current_node.data
    
    def mundur(self, steps):
        for i in range(steps):
            if self.current_node.prev_node is not None:
                self.current_node = self.current_node.prev_node
            else:
                break
        return self.current_node.data

linkedlist = LinkedList()

linkedlist.addElementHead("Jogja") #Jogja
linkedlist.addElementHead("Jakarta") #Jakarta - Jogja
linkedlist.addElementTail("Bali") #Jakarta - Jogja - Bali
linkedlist.addElementTail("Bandung") #Jakarta - Jogja - Bali - Bandung

print(linkedlist.maju(2)) #output: Bali
print(linkedlist.mundur(1)) #output: Jogja
print(linkedlist.maju(5)) #output: Bali
print(linkedlist.mundur(3)) #output: Bandung
