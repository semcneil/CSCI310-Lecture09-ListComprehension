"""
listComp.py
====================================
This is an example list comprehensions

| Author: Seth McNeill
| Date: 2025 September 09
"""

from timeit import Timer


def forsquares():
    squares = []
    for x in range(1000):
        squares.append(x**2)

    return squares

def listSquares():
   squares = [x**2 for x in range(1000)]
   return squares


if __name__ == '__main__':
  t1 = Timer("forsquares", "from __main__ import forsquares")
  print(f'for method: {t1.timeit(number=1000)} ms')
  t2 = Timer("listSquares", "from __main__ import listSquares")
  print(f'list comp method: {t2.timeit(number=1000)} ms')