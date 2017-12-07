#a=["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]
def calen(m,v):
    k=m
    z=1
    j=v
    a=["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]
    for i in range(k,k+j):
        a[i]=z
        z=z+1
        if j==a[i]: 
          g=(i+1)%7
        if a[i]<10:
         a[i]=" "+str(a[i])
    print "      SUN    MON     TUES   WED     THURS   FRI    SATUR" 
    print "     ", a[0], "    ",a[1], "   ", a[2], "    ",a[3], "   ", a[4], "    ",a[5], "   ",a[06]
    print "     ", a[7], "    ",a[8], "   ", a[9], "    ",a[10],"   ", a[11],"    ",a[12],"   ",a[13]
    print "     ", a[14],"    ",a[15],"   ", a[16],"    ",a[17],"   ", a[18],"    ",a[19],"   ",a[20]
    print "     ", a[21],"    ",a[22],"   ", a[23],"    ",a[24],"   ", a[25],"    ",a[26],"   ",a[27]
    print "     ", a[28],"    ",a[29],"   ", a[30],"    ",a[31],"   ", a[32],"    ",a[33],"   ",a[34]
    print "     ", a[35],"    ",a[36],"   ", a[37],"    ",a[38],"   ", a[39],"    ",a[40],"   ",a[41]
    print "*******************************************************************************"
    return g
l=raw_input("Enter the year\n")
l=int(l)
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
print "JANUARY"
p=calen(s,31)
print "FEBRAURY"
if x==1:
    q=calen(p,28)
else :
    q=calen(p,29)
print "MARCH"    
r=calen(q,31)
print "APRIL"
d=calen(r,30)
print "MAY"
w=calen(d,31)
print "JUNE"
l=calen(w,30)
print "JULY"
b=calen(l,31)
print "AUGUST"
i=calen(b,31)
print "SEPTEMBER"
o=calen(i,30)
print "OCTOBER"
m=calen(o,31)
print "NOVEMBER"
f=calen(m,30)
print "DECEMBER"
po=calen(f,31)
    

    
    

