a,b=raw_input("Enter the two numbers\n").split()
a=int(a)
b=int(b)
n=max(a,b)
b=min(a,b)
if n%b==0:
    print "The gcd is %d"%b
else :
    for i in range(b/2,0,-1):
        y=n%i
        x=b%i
        if x==0 is y==0:
            print "The gcd is %d"%i
            break
