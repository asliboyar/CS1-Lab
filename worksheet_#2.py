#2.check the given positive integer is power of 3.
a=int(input())
def pwr3(a):
  while a%3==0:
    a /= 3
  return a==1
print(pwr3(a))