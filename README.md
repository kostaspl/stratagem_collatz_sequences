# Longest Collatz Sequence [![Build Status](https://travis-ci.org/kostaspl/stratagem_collatz_sequences.svg?branch=master)](https://travis-ci.org/kostaspl/stratagem_collatz_sequences)
The aim of this project is to calculate the longest [collatz sequence](https://en.wikipedia.org/wiki/Collatz_conjecture) up to a given `n0` (`n_max`) and then return its length and last 20 elements.

## [collatz_baseline.py](collatz/collatz_baseline.py)
The baseline implementation iteratively calculates each sequence (from 1 to `n_max`), while keeping the longest sequence encountered.
It returns the length of the longest sequence, the corresponding `n0` and its last 20 elements.

## [collatz_o1.py](collatz/collatz_o1.py)
The first attempt at optimizing the code, led to utilizing bitwise operations. 
For example, to avoid conversion of the values produced when n is even, we perform the division by shifting right.
We also use bitwise operations to check if n is odd, instead of modulo.
Last, we remove the loop condition and move it into the case of odd numbers (as 1 is odd).

## [collatz_o2.py](collatz/collatz_o2.py)
This implementation is similar to `collatz_o1` but adds multiprocessing support.

Each process handles a different range of `n0`s, defined as `[ <process_number>, <process_number> + <number_of_processes>, <process_number> + 2 * <number_of_processes>, ... ]` up to `n_max`.

By default, the number of processes used is equal to the number of processors (or cores) on your system.

## [collatz_o3.py](collatz/collatz_o3.py)
The final implementation reverts back to a single process, but uses caching instead.
A dictionary works as a cache, storing each `n0`'s sequence length. This improves performance dramatically, but increases memory usage.
The cache does not store the intermediate sequences, only their lengths. In the end, the longest sequence is calculated.

## Performance
Here is the time required for a quick run (`n_max = 1000000`) on a machine equipped with an Intel Core i5-2500K processor and 16GB RAM, running Python 3.5.2 on Windows 10 64-bit:

Target | Time (s)
------------ | -------------
collatz_o3.py | 2.18
collatz_o2.py (4 processes) | 11.60
collatz_o2.py (2 processes) | 18.22
collatz_o1.py | 33.77
collatz_baseline.py | 52.52

For `n_max = 1000000`, the longest sequence is produced when `n0 = 837799`. 

Its length is 525 (or 524 steps) and its last 20 elements are `61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1`.

## Future improvements
One could consider extending the implementation that uses caching to utilize multiprocessing.
While that sounds promising, a quick implementation (using either Python's `Array` or `Manager().dict()`) showed major slow down.
A significant issue is the synchronization needed for the shared cache. 
Fine-grained locks could help with that.