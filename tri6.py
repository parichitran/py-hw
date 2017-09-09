import sys
n=raw_input("Enter the value\n")
n=int(n)
x=0
for i in range(2,n+2):
 for j in range(1,i):
  x=x+2
  print x,
 print ""
