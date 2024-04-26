import numpy as np

n, m = map(int, input().split())
fill_char = input().split()
array = np.full((n, m), fill_char[0])
if 'W' in fill_char or 'G' in fill_char or 'B' in fill_char:
    print("#Black&White")
else:
    print("#Color")

