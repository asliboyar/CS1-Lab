n = int(input())
def factorial(n):
  return 1 if n<2 else n*factorial(n-1)
t = int(input())
def cale(t):
  if not t:
    return 0
  else:
    return 1/factorial(t-1+cale(t-1))
  
print(factorial(n))
print(cale(t))
