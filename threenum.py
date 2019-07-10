(a,b,c) = tuple(input("Enter three number: "))

if a > b and a > c:
    print "\nA is Largest"
elif b > a and b > c:
    print "\nB is Largest"
elif c > a and c > b:
    print "\nC is Largest"
elif a == b and a > c:
    print "\nA and B are Largest"
elif a == c and a > b:
    print "\nA and C are Largest"
elif b == c and b > a:
    print "\nB and C are Largest"
else:
    print "\nAll are Equal"