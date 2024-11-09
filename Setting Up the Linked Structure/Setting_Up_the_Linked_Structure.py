class Node:
    def __init__(self, data, next=None):
        self.data = data  # Stores the value of the node
        self.next = next  # Points to the next node (None by default)

# Testing the Node class
if __name__ == "__main__":
    # Creating individual nodes
    node1 = Node(10)
    node2 = Node(20)
    
    # Linking nodes together
    node1.next = node2
    
    # Print the data in the linked nodes
    print("Node 1 data:", node1.data)  
    print("Node 2 data:", node2.data) 
    print("Node 1 next points to node with data:", node1.next.data)  

