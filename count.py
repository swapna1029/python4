def count(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print(count(150))
print(count(750))
