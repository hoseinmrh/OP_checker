class Node:
    def __init__(self, id, x, y, profit):
        self.id = id
        self.x = x
        self.y = y
        self.profit = profit
    
    def print_node(self):
        print(self.id,"   ", self.x,"   ", self.y,"    ", self.profit)
