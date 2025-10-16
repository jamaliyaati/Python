queue = [""] * 10
tail =  0
header = -1

def enqueue(value):
    global queue, tail, header

    if tail < len(queue):
        queue[tail] = value
        tail =+ 1

        if header == -1:
            header = 0
        return True
    else:
        return False


def dequeue():
    global queue, header, tail

    if header == -1:
        return False

    elif header == tail:
        header = -1
        tail = 0
        return False

    else:
        header =+1
        return True