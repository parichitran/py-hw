z=0
def leap(o):
 k=o
 if k%4!=0:
    print "Its not a leap year" 
    z=z+1
    return z
 elif k%100!=0:
    print "Its a leap year"
    z=z+2
    return z
 elif k%400!=0:
    print "Its not a leap year"
    z=z+1 
    return z
 else :
    print "Its a leap year"
    z=z+2 
    return z
n=raw_input("Enter the year")
n=int(n)
for i in range(1,n): 
 m=leap(i)
print m
