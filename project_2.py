a=int(input("How many Fibonacci numbers would you like to print? (Enter a positive value):")) or 12
m=[0,1]
if a>=0:
  while len(m) <=a:
     d=m[len(m)-1]+m[len(m)-2]
     m.append(d)
  print(m)
else:
   print("The value entered is in negative")

