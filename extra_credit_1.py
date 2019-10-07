a=int(input())
b=int(input())
c=int(input())
n=int(input())
def check_fermat(a, b, c, n):
  while n>2:
    if a**n+b**n==c**n:
      print("Holy smokes, Fermat was wrong!")
    else:
      print("No that doesn't work.")
  return check_fermat