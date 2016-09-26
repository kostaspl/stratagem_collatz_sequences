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
Here is the time required for a quick run (`n_max = 1M`) on a machine equipped with an Intel Core i5-2500K processor and 16GB RAM, running Python 3.5.2 on Windows 10 64-bit:

Target | Time (s)
------------ | -------------
collatz_o3.py | 2.18
collatz_o2.py (4 processes) | 11.60
collatz_o2.py (2 processes) | 18.22
collatz_o1.py | 33.77
collatz_baseline.py | 52.52

For `n_max = 1M`, the longest sequence is produced when `n0 = 837799`.  
Its length is 525 (or 524 steps) and its last 20 elements are `61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1`.

Given the nature of this problem, calculating its time complexity is not possible, as it has not been proven to be true for every integer. 
To predict the time needed for `n_max = 100M`, we can extrapolate from runs with smaller `n_max`.  

`n_max` | Approximate Average Sequence Length | Approximate Number of Iterations | Relative Number of Iterations (compared to row below) |
------------:|:------------:| -------------:|:-------------:|
100M | 180 (+24) | 18000000000 | 11.53x |
10M | ~156 (+24) | ~1560000000 | 11.81x |
1M | ~132 (+23) | ~132000000 | 12.11x |
100K | ~109 (+23) | ~10900000 | 12.67x |
10K | ~86 | ~860000 | - |

As a result, `n_max = 100M` should be around 136 times slower than `n_max = 1M`.

## Future Improvements
One could consider extending the implementation that uses caching to utilize multiprocessing.
While that sounds promising, a quick implementation (using either Python's `Array` or `Manager().dict()`) showed major slow down.
A significant issue is the synchronization needed for the shared cache. 
Fine-grained locks could help with that.

## Bonus
[bonus](bonus/) folder contains 2 Cython implementations.  
[cython_impl.pyx](bonus/cython_impl.pyx) is equivalent to [collatz_o1.py](collatz/collatz_o1.py),
while [cython_mp_impl.pyx](bonus/cython_mp_impl.pyx) is equivalent to [collatz_o2.py](collatz/collatz_o2.py) as it uses `multiprocessing`.

Cython implementations have not yet been integrated in tests, but here are some performance figures.  
For `n_max = 1M`:

Target | Time (s)
------------ | -------------
cython_impl.pyx | 0.23
cython_mp_impl.pyx | 0.23

And here's a full comparison for `n_max = 10M`:

Target | Time (s)
------------ | -------------
cython_mp_impl.pyx (4 processes) | 0.89
cython_impl.pyx | 2.30
collatz_o3.py | 19.79
collatz_o2.py (4 processes) | 117.25
collatz_o1.py | 364.57
collatz_baseline.py | 624.41