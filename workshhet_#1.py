#1.check the given positive integer is power of 2.
a=int(input())
def pwr2(a):
  while a%2==0:
    a /= 2
  return a==1
print(pwr2(a))
