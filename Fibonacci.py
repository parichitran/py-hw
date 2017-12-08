x=raw_input("Enter the value\n")
x=int(x)
print "1",
a=1
b=0
for i in range(1,x):
 c=a+b
 b=a
 a=c
 print c,
