queue = [""] * 10
items = 0
head = 0
tail = 0


def enqueue(value):
    global head, tail, items, queue
    if items == len(queue):
        print("queue full")
        return False
    else:
        queue[tail] = value
        tail = (tail + 1) % len(queue)
        items += 1
        return True

def dequeue():
    global head, tail, items, queue
    if items == 0:
        return False
    else:
        value = queue[head]
        head = (head + 1) % len(queue)
        items -= 1
        return True, print("returned value:", value)


