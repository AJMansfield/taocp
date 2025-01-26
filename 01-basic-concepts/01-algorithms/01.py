a, b, c, d = (c for c in "ABCD")

target = b,c,d,a

temp = a
a = b
b = c
c = d
d = temp

assert (a, b, c, d) == target
