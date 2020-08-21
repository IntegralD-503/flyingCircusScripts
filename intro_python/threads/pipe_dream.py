from multiprocessing import Process, Pipe, Queue

def print_queue(q):
    """
    function to print queue elements
    """
    print("Queue elements:")
    while not q.empty():
        print(q.get())
        print("Queue is now empty!")


def tripler(mylist, conn):
    for ind, item in enumerate(mylist):
        mylist[ind] = item * 3
    # sends or returns data through the pipe -as child_conn
    conn.send(mylist)
    # closes connection to pipe - so others may use it next
    conn.close()


if __name__ == '__main__':
    # sets pipe ends
    parent_conn, child_conn = Pipe()
    nums = [3, 4, 5, 6]
    p = Process(target=tripler, args=(nums, child_conn,))
    p.start()
    # print what parent process received
    print(parent_conn.recv())   
    p.join()

