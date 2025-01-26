
def ver_1(m, n):
  while True:
    r = m % n #e1
    if r == 0: #e2
      return n
    m, n = n, r #e3

assert ver_1(119, 544) == 17

def ver_2(m, n):
  if m < n:
    m, n = n, m # e0

  while True:
    r = m % n # e1
    if r == 0: #e2
      return n
    m, n = n, r #e3

assert ver_2(119, 544) == 17

def iterated(f):
  def curried(*args):
    while True:
      state = f(*args)
      if state == args:
        return state
      args = state
  return curried

@iterated
def f(*args):
  if len(args) == 1:
    n, = args
    return (n,)
  elif len(args) == 2:
    m, n = args
    return (m, n, 0, 1)
  elif len(args) == 4:
    m, n, rp, step = args
    if step == 1:
      return (m, n, m%n, 2)
    elif step == 2:
      if rp == 0:
        return (n,)
      else:
        return (m, n, rp, 3)
    elif step == 3:
      return (n, rp, rp, 1)
    else:
      assert False
  else:
    assert False

assert f(119, 544) == (17,)