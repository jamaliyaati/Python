class node:
    def __init__(self):
        self.data = ""
        self.Pointer = None

size = 10

def createlist():

    global List, HeadPointer, FreePointer
    
    List = [node() for i in range(size)]
    
    for i in range(size-1):
        List[i].Pointer = i + 1

    FreePointer = 0
    HeadPointer = None

###############################################

def append(NewData):

    global List, HeadPointer, FreePointer

#   check if there is space is in the list
    if FreePointer is None:
        print("list is full")
        return False

    else:

#       Take free node from FreeList Pointer        
        NewPointer = FreePointer
        FreePointer = List[NewPointer].Pointer

#       Add new data to node and mark it as last node for now        
        List[NewPointer].data = NewData
        List[NewPointer].Pointer = None

#       Check if list is empty and new node becomes headpointer
        if HeadPointer is None:
            HeadPointer = NewPointer

#       otherwise find end of list
        else:
            Pointer = HeadPointer

#           identify last node to attach it to new node
            while Pointer is not None:
                LastPointer = Pointer
                Pointer = List[Pointer].Pointer 

#           attach newnode to the end
            List[LastPointer].Pointer = NewPointer

###############################################

def prepend(NewData):
    
    global List, HeadPointer, FreePointer

#   check if there is space is in the list
    if FreePointer is None:
        print("list is full")
        return False

    else:

#       Take free node from FreeList Pointer        
        NewPointer = FreePointer
        FreePointer = List[NewPointer].Pointer

#       Add new data to node and mark it as last node for now        
        List[NewPointer].data = NewData
        List[NewPointer].Pointer = None

#       Check if list is empty then new node becomes headpointer
        if HeadPointer is None:
            HeadPointer = NewPointer

#       otherwise add it to the start of the list
        else:
            List[NewPointer].Pointer = HeadPointer
            HeadPointer = NewPointer

###############################################

def insert(NewData,After):

    global List, HeadPointer, FreePointer, size

#   check if list is full
    if FreePointer is None:
        print("list is full")
        return False
    
#   check if list is empty
    if HeadPointer is None:
        print("list is empty")
        return False

#   Check if data exists so that we can insert after it
    Found = False
    Pointer = HeadPointer
    for i in List:
        
        if Pointer is None:
            break
        if List[Pointer].data == After:
            Found = True
            break
        Pointer = List[Pointer].Pointer
#   if doesnt exist abort
    if not Found:
        print("Data not found")
        return False

#   Take a free node
    NewPointer = FreePointer

#   Update the FreePointer
    FreePointer = List[NewPointer].Pointer

#   Fill free node with data
    List[NewPointer].data = NewData
    List[NewPointer].Pointer = None

#   Insert new data pointer after Pointer
    NextPointer = List[Pointer].Pointer
    List[Pointer].Pointer = NewPointer
    List[NewPointer].Pointer = NextPointer

###############################################

def search(data):
    global List, HeadPointer, FreePointer

    Found = False

#   Pointer keeps track of the current node index
    Pointer = HeadPointer

#   Loop through every index of list
    for i in range(len(List)): 

#   if Pointer is none means list is empty
        if Pointer is None:
            break

#   If current node has data stop the loop
        if List[Pointer].data == data:
            Found = True
            break
#       Move to next node
        Pointer = List[Pointer].Pointer

    if not Found:
        print("Data not found")
        return False
    else:
        print(f"Data '{data}' found at node pointer {Pointer}")
        return True


###############################################

def delete(data):
    global List, HeadPointer, FreePointer

#    check if list is empty
    if HeadPointer is None:
        print("List is empty, nothing to delete")
        return False

#   Keep track of node before current node
    Pointer = HeadPointer
    Previous = None 

    # Search for the node to delete
    for _ in range(len(List)):

#       Pointer is pointing to none so end of list reached
        if Pointer is None:
            break

#       if data is found stop the loop
        if List[Pointer].data == data:
            break
        Previous = Pointer
        Pointer = List[Pointer].Pointer
  
#   abort if data not found
    if Pointer is None or List[Pointer].data != data:
        print("Data not found")
        return False

#   Remove the node from the linked list
    if Previous is None:
        
#       Delete the headnode
        HeadPointer = List[Pointer].Pointer
    else:
        List[Previous].Pointer = List[Pointer].Pointer

#   Add the deleted node back to the free list
    List[Pointer].Pointer = FreePointer
    FreePointer = Pointer

#   clear data
    List[Pointer].data = ""
    print(f"Deleted '{data}' successfully")
    return True

###############################################

def displaylist():

    global List, HeadPointer, FreePointer

    Pointer = HeadPointer
    while Pointer is not None:
        print(List[Pointer].data,end=" ")
        Pointer = List[Pointer].Pointer



def test():
    createlist()
    append("one")
    append("two")
    append("three")
    displaylist()
    insert("twopointfive","two")
    displaylist()
    search("one")

test()


    
