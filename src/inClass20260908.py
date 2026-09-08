"""
inClass20260908.py
====================================
This is the work we did in class today.

| Author: Seth McNeill
| Date: 2026 September 08
"""

import timeit


def test1():
    """
    Build a list using a for loop.
    """
    myList = []
    for ii in range(1_000):
        myList = myList + [ii]

def test2():
    """
    Creates list using append()
    """
    myList = []
    for ii in range(1_000):
        myList.append(ii)

def test3():
    """ 
    Creates list using list comprehension
    """
    myList = [ii for ii in range(1_000)]

def test4():
    """ 
    Creates list using list of range
    """
    myList = list(range(1_000))

if __name__ == "__main__":
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print(f"Concat took {t1.timeit(number=1000)} milliseconds")
    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print(f"append took {t2.timeit(number=1000)} milliseconds")
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print(f"list comp took {t3.timeit(number=1000)} milliseconds")
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print(f"list range took {t4.timeit(number=1000)} milliseconds")


    
    x = list(range(1_000_000))
    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    print(f"After popzero, x length is : {len(x)}")
    popend = timeit.Timer("x.pop", "from __main__ import x")
    print(f"Popping at zero took: {popzero.timeit(number=1000)}")
    print(f"Popping at end took: {popend.timeit(number=1000)}")
