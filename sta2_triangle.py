import sys
n=raw_input("Enter the value\n")
n=int(n)
m="*"
for i in range(n,0,-1):
 print m,
 for j in range(1,i):
  print " ",
 sys.stdout.softspace=0
 print m
 m="*"
 for k in range(0,n-j):
    m=m+"*"

    
 
    
    
