#8.find the length of last word.
a=input()
def len_of_last_word(a):
  w=a.split()
  if len(w)==0:
    return 0
  return len(w[-1])
print(len_of_last_word(a))
