a=int(input("Number of elements you want to enter"))
c=[]
for i in range (0,a):
   b=int(input("Enter elements of list"))
   c.append(b)
print("input",c)
for elements in c:
    if elements <0:
        c.remove(elements)
print("output",c)