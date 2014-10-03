name=raw_input("what is your name ")
while True:
    a=raw_input("type a number ")
    b=raw_input("type a number ")
    a=int(a)
    b=int(b)
    c=a*b
    print "{name}, the answer is {product}".format(name=name,product=c)
