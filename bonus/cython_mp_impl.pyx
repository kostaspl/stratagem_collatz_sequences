import time
from multiprocessing import Queue, Process, cpu_count

def calculate_collatz_sequences(q, n_max, n_proc, cpus):
    cdef int longest_sequence_len = 0
    cdef int longest_n0 = 0
    cdef long long int n = 0
    cdef int n0 = 0
    cdef int curr_len = 0
    
    for n0 in range(n_proc + 1, n_max + 1, cpus):
        n = n0
        curr_len = 1

        while True:
            if n & 1:
                if n == 1:
                    break
                n = 3 * n + 1
            else:
                n = n >> 1
            curr_len = curr_len + 1

        if curr_len > longest_sequence_len:
            longest_sequence_len = curr_len
            longest_n0 = n0
	    
    n = longest_n0
    longest_sequence = [n]
    while True:
        if n & 1:
            if n == 1:
                break
            n = 3 * n + 1
        else:
            n = n >> 1
        longest_sequence.append(n)

    q.put([longest_sequence_len, longest_n0, longest_sequence[-20:]])

    
def calculate_collatz_sequences_mp(n_max, cpus=cpu_count()):
    q = Queue()
    print("Will use {} CPUs...".format(cpus))

    procs = []
    args = []

    for i in range(cpus):
        args.append((q, n_max, i, cpus))

    for i in range(cpus):
        procs.append(Process(target=calculate_collatz_sequences, args=args[i]))

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    results = []
    while not q.empty():
        results.append(q.get())

    results.sort(key=lambda x: x[0])
    
    return results[-1]