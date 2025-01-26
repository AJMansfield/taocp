
def algorithm_f(m, n):
  while True:
    if m > n:
      m = m % n
      if m == 0:
        return n
    else:
      n = n % m
      if n == 0:
        return m

assert algorithm_f(119, 544) == 17
