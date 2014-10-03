while True:
    a=raw_input("type a number ")
    b=raw_input("type a number ")
    a=int(a)
    b=int(b)
    print "1=add"
    print "2=subtract"
    print "3=multiply"
    print "4=divide"
    d=raw_input("what do you want to do? ")
    if d=="1":
        c=a+b
    if d=="2":
        c=a-b
    if d=="3":
        c=a*b
    if d=="4":
        c=a/b
    print "the answer is", c

