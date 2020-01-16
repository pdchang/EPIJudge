from typing import List

from test_framework import generic_test

# O(n log n) cause sort
def h_index(citations: List[int]) -> int:   
    n = len(citations)
    citations.sort()
    for i, j in enumerate(citations):
        if j >= n - i:
            return n - i
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
