import time
from multiprocessing import Queue, Process, cpu_count

def calculate_collatz_sequences(q, n_max, n_proc, cpus):
    longest_sequence_len = 0
    
    for n0 in range(n_proc + 1, n_max + 1, cpus):
        n = n0
        sequence = [n]
        
        while True:
            if n & 1:
                if n == 1:
                    break
                n = 3 * n + 1
            else:
                n = n >> 1
            sequence.append(n)

        if len(sequence) > longest_sequence_len:
            longest_sequence_len = len(sequence)
            longest_sequence = sequence
            longest_n0 = n0

    q.put([longest_sequence_len, longest_n0, longest_sequence[-20:]])

    
def calculate_collatz_sequences_mp(n_max, cpus=cpu_count()):
    q = Queue()
    print("Will use", cpus, "CPUs...")

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
    
    
if __name__ == "__main__":
    start_time = time.time()
    
    result = calculate_collatz_sequences_mp(1000000)
    
    print("Longest sequence is for n0 =", result[1])
    print("The last", min(result[0], 20), "elements of this sequence are", result[2][-20:])
    print("Its length is", result[0])
    
    print("--- %s seconds ---" % (time.time() - start_time))
