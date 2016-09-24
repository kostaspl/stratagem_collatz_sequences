import pytest
from collatz import collatz_baseline, collatz_o1, collatz_o2, collatz_o3

results = {
    10: [20, 9, [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]],
    1000: [179, 871, [61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]],
    1000000: [525, 837799, [61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
    }

def test_baseline():
    for n0_max in results:
        result = collatz_baseline.calculate_collatz_sequences(n0_max)
        assert result == results[n0_max]

def test_o1():
    for n0_max in results:
        result = collatz_o1.calculate_collatz_sequences(n0_max)
        assert result == results[n0_max]

def test_o2():
    for n0_max in results:
        for procs in range(1, 4):
            result = collatz_o2.calculate_collatz_sequences_mp(n0_max, procs)
            assert result == results[n0_max]

def test_o3():
    for n0_max in results:
        result = collatz_o3.calculate_collatz_sequences(n0_max)
        assert result == results[n0_max]
