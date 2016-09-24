import time

def calculate_collatz_sequences(n_max):
    longest_sequence_len = 0
    sequences_length_cache = {}
    
    for n0 in range(1, n_max + 1):
        n = n0
        curr_len = 1
        extra_len = 0
        
        while True:
            if n in sequences_length_cache:
                extra_len = sequences_length_cache[n] - 1
                break
            else:                
                if n & 1:
                    if n == 1:
                        break
                    n = 3 * n + 1
                else:
                    n = n >> 1
                curr_len = curr_len + 1

        curr_len = curr_len + extra_len
        sequences_length_cache[n0] = curr_len

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

if __name__ == "__main__":
    start_time = time.time()

    result = calculate_collatz_sequences(1000000)
    
    print("Longest sequence is for n0 =", result[1])
    print("The last", min(result[0], 20), "elements of this sequence are", result[2][-20:])
    print("Its length is", result[0])
    
    print("--- %s seconds ---" % (time.time() - start_time))
