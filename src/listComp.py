"""
listComp.py
====================================
This is an example list comprehensions

Figure took 29 min, 4 seconds to make.

| Author: Seth McNeill
| Date: 2025 September 09
"""
from timeit import Timer
import timeit
import matplotlib.pyplot as plt  # to plot results (uv pip install matplotlib)
from datetime import datetime

def forsquares():
    """Does squares of a list of numbers using a for loop"""
    squares = []
    for x in range(100):
        squares.append(x**2)

    return squares

def listSquares():
   """Does squares of a list of numbers using list comprehension"""
   squares = [x**2 for x in range(100)]
   return squares

# examples from https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/Lists.html
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))

if __name__ == '__main__':
  start_time = datetime.now()

  t1 = Timer("test1()", "from __main__ import test1")
  print("concat ",t1.timeit(number=1000), "milliseconds")
  t2 = Timer("test2()", "from __main__ import test2")
  print("append ",t2.timeit(number=1000), "milliseconds")
  t3 = Timer("test3()", "from __main__ import test3")
  print("comprehension ",t3.timeit(number=1000), "milliseconds")
  t4 = Timer("test4()", "from __main__ import test4")
  print("list range ",t4.timeit(number=1000), "milliseconds")

  print("Popping at zero")
  x = list(range(2000000))
  print(popzero.timeit(number=1000))
  print("Popping at end")
  x = list(range(2000000))
  print(popend.timeit(number=1000))

  t1 = Timer("forsquares()", "from __main__ import forsquares")
  print(f'for method: {t1.timeit(number=1000000)} ms')
  t2 = Timer("listSquares()", "from __main__ import listSquares")
  print(f'list comp method: {t2.timeit(number=1000000)} ms')

  listLen = []
  popEndList = []
  popZeroList = []
  print("    len    pop(0)   pop()")
  try:
    for i in range(1000000,100000001,1000000):
    #   for i in range(1000000,10000001,1000000):
        x = list(range(i))
        pt = popend.timeit(number=1000)
        x = list(range(i))
        pz = popzero.timeit(number=1000)
        print("%15.0f, %15.5f, %15.5f" %(i,pz,pt))
        listLen.append(i)
        popEndList.append(pt)
        popZeroList.append(pz)
  except KeyboardInterrupt:
      print("Stopping processing")

  end_proc = datetime.now()
  print(f"Processing took: {end_proc - start_time}")

  fig, ax = plt.subplots(figsize=(11,8.5))
  plt.rcParams['font.size'] = '18'
  for label in (ax.get_xticklabels() + ax.get_yticklabels()):
      label.set_fontsize(18)
  ax.plot(listLen, popEndList, '-bo', label='popEnd')
  ax.plot(listLen, popZeroList, '-ro', label='popZero')
  plt.xlabel('Length of List', fontsize=20)
  plt.ylabel(f'Avg time', fontsize=20)
  plt.grid()
  plt.title('Python List Pop Times', fontsize=24)
  plt.legend()
  plt.savefig('listPop.png')
  plt.show()