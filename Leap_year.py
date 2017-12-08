z=0
def leap(o):
 k=o
 if k%4!=0:
    print "Its not a leap year" 
 elif k%100!=0:
    print "Its a leap year"
 elif k%400!=0:
    print "Its not a leap year"
 else :
    print "Its a leap year"
n=raw_input("Enter the year")
n=int(n) 
m=leap(n)
