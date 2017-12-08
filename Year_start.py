l=raw_input("Enter the year\n")
l=int(l)
n=0
for y in range(1,l+1):
 z=0   
 if y%4!=0:
    n=n+1
    z=z+1
 elif y%100!=0:
    n=n+2
    z=z+2
 elif y%400!=0:
    n=n+1
    z=z+1
 else :
    n=n+2
    z=z+2
s=n%7
print "The given year starts with ",
if s==0:
    print "sunday"
elif s==1:
 print "monday"
elif s==2:
    print " tuesesday"
elif s==3:
    print "wedsday"
elif s==4:
    print " thuysday"
elif s==5:
    print "friday"
elif s==6:
    print " saturday" 
