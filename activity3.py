print("enter the marks of 5 subjects")
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if avg>=91 and avg<=100:
    print("your grade is a1")
elif avg>=81 and avg<=90:
    print("your grade is a2")
elif avg>=71 and avg<=80:
    print("your grade is b1")
elif avg>=61 and avg<=70:
    print("your grade is b2")
elif avg>=51 and avg<=60:
    print("your grade is c1")
elif avg>=41 and avg<=50:
    print("your grade is c2")
elif avg>=31 and avg<=40:
    print("your grade is d")
elif avg>=21 and avg<=30:
    print("your grade is e1")
elif avg>=11 and avg<=20:
    print("your grade is e2")
else:
    print("invaild input")
