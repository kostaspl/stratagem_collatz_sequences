import cython_impl
import time

if __name__ == "__main__":
    start_time = time.time()
    
    result = cython_impl.calculate_collatz_sequences(1000000)
    
    print("Longest sequence is for n0 =", result[1])
    print("The last", min(result[0], 20), "elements of this sequence are", result[2][-20:])
    print("Its length is", result[0])
    
    print("--- %s seconds ---" % (time.time() - start_time))
