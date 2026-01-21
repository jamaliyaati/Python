
size = 10

class node:
    def __init__(self):
        # Initializing data as empty string and pointer as -1 (null)
        self.data = ""
        self.nextp = -1

class Linkedlist:
    def __init__(self):
        # Create a static array of 'size' nodes
        self.thislist = [node() for _ in range(size)]

        # Initialize the 'Free List': link each node to the next index
        # This allows the program to know where the next empty space is
        for x in range(size):
            self.thislist[x].nextp = x + 1
        
        # The last node in the free list points to -1 (end of pool)
        self.thislist[size-1].nextp = -1
        
        # freepointer: tracks the first available empty node
        # startpointer: tracks the first node containing actual data
        self.freepointer = 0
        self.startpointer = -1

    def insert(self, s):
        # Check if there is space available in the array
        if self.freepointer != -1:
            # 1. Pick the first node from the free list
            newnodeptr = self.freepointer
            self.thislist[newnodeptr].data = s
            
            # 2. Update freepointer to the next available empty slot
            self.freepointer = self.thislist[self.freepointer].nextp

            # --- CASE A: The list is currently empty ---
            if self.startpointer == -1:
                self.thislist[newnodeptr].nextp = -1
                self.startpointer = newnodeptr
            
            else:
                # --- CASE B: Find the alphabetical/numerical position ---
                previouspointer = -1
                currentpointer = self.startpointer

                # Traverse to find the correct insertion point (maintains sorted order)
                while currentpointer != -1 and self.thislist[currentpointer].data < s:
                    previouspointer = currentpointer
                    currentpointer = self.thislist[currentpointer].nextp
                
                # If previouspointer is still -1, the new node becomes the NEW head
                if previouspointer == -1:
                    self.thislist[newnodeptr].nextp = self.startpointer
                    self.startpointer = newnodeptr
                else:
                    # Insert the node between 'previous' and 'current'
                    self.thislist[newnodeptr].nextp = self.thislist[previouspointer].nextp
                    self.thislist[previouspointer].nextp = newnodeptr
        else:
            # No more slots available in the static array
            print("list is full")

    def search(self, target):
        # Start at the beginning of the list
        currentpointer = self.startpointer
        
        # Traverse the list while there are nodes to check
        while currentpointer != -1:
            # Check if the current node's data matches the target
            if self.thislist[currentpointer].data == target:
                # Value found! Return the index (pointer) where it exists
                return currentpointer
            
            # If the current node's data is already "greater" than the target,
            # we can stop early because the list is sorted.
            if self.thislist[currentpointer].data > target:
                break
                
            # Move to the next node in the sequence
            currentpointer = self.thislist[currentpointer].nextp
            
        # If the loop finishes without returning, the value is not in the list
        return -1