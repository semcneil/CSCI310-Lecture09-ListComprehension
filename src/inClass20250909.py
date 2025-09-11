
from datetime import datetime
from timeit import Timer


t1 = datetime.now()
x = [num**3 for num in range(52) if num % 3 != 0]
t2 = datetime.now()
print(f'It took {(t2-t1).total_seconds()} seconds')

popzero = Timer("x.pop(0)",
                       "from __main__ import x")
popend = Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print(f'popzero took {popzero.timeit(number=1000)}')

x = list(range(2000000))
print(f'popend took {popend.timeit(number=1000)}')