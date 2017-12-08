n=raw_input("Enter the value\n")
n=int(n)
m="*"
for i in range(n,0,-1):
 for j in range(1,i):
  print "",
 print m
 m="*"
 for k in range(0,n-j):
    m=m+"*"
    
 
    
    
