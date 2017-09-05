n=raw_input("Enter the value\n")
n=int(n)
m=1
x=2
for i in range(n,0,-1):
 for j in range(1,i):
  print "",
 print m
 for k in range(x,x+2,2):
    m=(10**k)+1
 x=x+2
    
    
