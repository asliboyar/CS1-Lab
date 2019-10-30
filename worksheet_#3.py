#3.check the given positive integer is power of 4.
a=int(input())
def pwr4(a):
  while a%4==0:
    a /= 4
  return a==1
print(pwr4(a))