#a=["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]
def calen(m,v,mm,tt,da):
    k=m
    z=1
    j=v
    mo=mm
    ta=tt
    dy=da
    a=["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]
    for i in range(k,k+j):
        a[i]=z
        z=z+1
        if j==a[i]: 
          g=(i+1)%7
        if mo==ta:
            if a[i]==dy:
                tk=i%7
                print "The given day is",
                if tk==0:
                  print "SUNDAY"
                elif tk==1:
                  print "MONDAY"
                elif tk==2:
                  print " TUESDAY"
                elif tk==3:
                  print "WEDNESDAY"
                elif tk==4:
                  print "THURSDAY"
                elif tk==5:
                  print "FRIDAY"
                elif tk==6:
                  print "SATURDAY" 
                import sys
                sys.exit()
    return g
l,mn,de=raw_input("Enter the year month and date(yy mm dd) in numbers\n").split()
l=int(l)
mn=int(mn)
de=int(de)
n=0
for y in range(1,l+1):
 x=0   
 if y%4!=0:
    n=n+1
    x=x+1
 elif y%100!=0:
    n=n+2
    x=x+1
 elif y%400!=0:
    n=n+1
    x=x+1
 else :
    n=n+2
    x=x+2
s=n%7
#print "JANUARY"
p=calen(s,31,1,mn,de)
#print "FEBRAURY"
if x==1:
    q=calen(p,28,2,mn,de)
else :
    q=calen(p,29,2,mn,de)
#print "MARCH"    
r=calen(q,31,3,mn,de)
#print "APRIL"
d=calen(r,30,4,mn,de)
#print "MAY"
w=calen(d,31,5,mn,de)
#print "JUNE"
l=calen(w,30,6,mn,de)
#print "JULY"
b=calen(l,31,7,mn,de)
#print "AUGUST"
i=calen(b,31,8,mn,de)
#print "SEPTEMBER"
o=calen(i,30,9,mn,de)
#print "OCTOBER"
m=calen(o,31,10,mn,de)
#print "NOVEMBER"
f=calen(m,30,11,mn,de)
#print "DECEMBER"
po=calen(f,31,12,mn,de)
