import sys
n=raw_input("Enter the value\n")
n=int(n)
for i in range(1,n+1):
 for j in range(0,i):
  print "*",
  sys.stdout.softspace=0
 print ""
