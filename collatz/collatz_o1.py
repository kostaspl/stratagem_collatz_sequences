import time

def calculate_collatz_sequences(n_max):
    longest_sequence_len = 0

    for n0 in range(1, n_max + 1):
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

    return [longest_sequence_len, longest_n0, longest_sequence[-20:]]
    
if __name__ == "__main__":
    start_time = time.time()
    
    result = calculate_collatz_sequences(1000000)
    
    print("Longest sequence is for n0 =", result[1])
    print("The last", min(result[0], 20), "elements of this sequence are", result[2][-20:])
    print("Its length is", result[0])
    
    print("--- %s seconds ---" % (time.time() - start_time))
