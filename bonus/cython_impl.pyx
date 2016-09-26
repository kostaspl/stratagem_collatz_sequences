import time

def calculate_collatz_sequences(int n_max):
    cdef int longest_sequence_len = 0
    cdef int longest_n0 = 0
    cdef long long int n = 0
    cdef int n0 = 0
    cdef int curr_len = 0
    
    for n0 in range(1, n_max + 1):
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

    return [longest_sequence_len, longest_n0, longest_sequence[-20:]]
