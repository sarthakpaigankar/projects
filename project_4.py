from collections import OrderedDict 
import numpy as np

def most_frequent(g):
   g= list(g)
   d={}
   for elements in g:
      d[elements] = g.count(elements)   
   keys=list(d.keys()) 
   values =list(d.values())
   sdv= np.array(values)
   k=np.argsort(sdv)[::-1]
   sd ={keys[i]:values[i] for i in k}
   return sd  
   



a =input("Please enter a string")

c=most_frequent(a)

for key, value in c.items():

    print(key,value)