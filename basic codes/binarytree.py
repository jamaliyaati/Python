class node:
    def __init__(self):
        self.data = ""
        self.left = None
        self.right = None


size = 10

def InitializeTree():
    global Tree, FreePointer, RootPointer

    Tree = [node() for _ in range(size)]

    for i in range(size - 1):
        Tree[i].left = i + 1     # free list

    Tree[size - 1].left = None
    FreePointer = 0
    RootPointer = None


def findinsertpoint(newdata):
    global Tree, RootPointer

    Pointer = RootPointer
    PreviousPointer = None

    while Pointer is not None:
        PreviousPointer = Pointer
        CurrentData = Tree[Pointer].data

        if newdata > CurrentData:
            direction = "right"
            Pointer = Tree[Pointer].right
        else:
            direction = "left"
            Pointer = Tree[Pointer].left

    return PreviousPointer, direction


def Add(newdata):
    global Tree, FreePointer, RootPointer

    if FreePointer is None:
        print("Tree is full")
        return

    NewPointer = FreePointer
    Tree[NewPointer].data = newdata
    FreePointer = Tree[NewPointer].left
    Tree[NewPointer].left = None
    Tree[NewPointer].right = None

    if RootPointer is None:
        RootPointer = NewPointer
        return

    Pointer, direction = findinsertpoint(newdata)

    if direction == "left":
        Tree[Pointer].left = NewPointer
    else:
        Tree[Pointer].right = NewPointer


def TraverseTree(Pointer=None):
    global Tree, RootPointer

    if Pointer is None:
        Pointer = RootPointer
        if Pointer is None:
            return

    Left = Tree[Pointer].left
    Right = Tree[Pointer].right

    if Left is not None:
        TraverseTree(Left)

    print(Tree[Pointer].data)

    if Right is not None:
        TraverseTree(Right)


def test():
    InitializeTree()

    for Animal in """
mouse
cat
dog
hello
bye
wher
jiraf
bro
gas
wall
tree
ghost
""".split("\n"):
        if Animal.strip() != "":
            Add(Animal.strip())

    TraverseTree()

test()