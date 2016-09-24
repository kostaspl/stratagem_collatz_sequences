import pytest
from collatz import collatz_baseline, collatz_o1, collatz_o2, collatz_o3

def test_benchmark_baseline(benchmark):
    benchmark.pedantic(collatz_baseline.calculate_collatz_sequences, args=(1000000,), iterations=1, rounds=1)

def test_benchmark_o1(benchmark):
    benchmark.pedantic(collatz_o1.calculate_collatz_sequences, args=(1000000,), iterations=1, rounds=1)

def test_benchmark_o2(benchmark):    
    benchmark.pedantic(collatz_o2.calculate_collatz_sequences_mp, args=(1000000,), iterations=1, rounds=1)

def test_benchmark_o3(benchmark):
    benchmark.pedantic(collatz_o3.calculate_collatz_sequences, args=(1000000,), iterations=1, rounds=1)
