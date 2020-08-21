from multiprocessing import Process, Pipe, Queue

def print_queue(q):
    """
    function to print queue elements
    """
    print("Queue elements:")
    while not q.empty():
        print(q.get())
        print("Queue is now empty!")


def triplerQueue(mylist, q):
    """
    function to triple items in a given list
    """
    # append triples of mylist to queue
    for num in mylist:
        q.put(num*3)

def triplerPipe(mylist, conn):
    for ind, item in enumerate(mylist):
        mylist[ind] = item * 3
    # sends or returns data through the pipe -as child_conn
    conn.send(mylist)
    # closes connection to pipe - so others may use it next
    conn.close()



if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4]

    # creating multiprocessing Queue
    q = Queue()

    # creating new processes
    p1 = Process(target=triplerQueue, args=(mylist, q))
    p2 = Process(target=print_queue, args=(q,))

    # running process p1 to square list
    p1.start()
    p1.join()

    # running process p2 to get queue elements
    p2.start()
    p2.join()

