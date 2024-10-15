''' to int '''
a=10.5
print(int(a))
b=True
c=False
print(int(b))
print(int(c))
d="10"
print(int(d))       # but cant convert "hello" to int. Only base 10 number can convert string to int

''' to float '''

a=10
print(float(a))
b=True
c=False
print(float(b))
print(float(c))
d="10.5"
print(float(d))

''' to complex '''
a=10
print(complex(a))
b=10.5
print(complex(b))
c=True
print(complex(c))
d="10"
print(complex(d))
e="10.6"
print(complex(e))
f="10j"
print(complex(f))

''' to bool '''
print(bool(1))
print(bool(0))
print(bool(10.121))
print(bool(0.01))
print(bool("aayush"))
print(bool(""))
print(bool(2+2j))

''' to str '''
a=10
print(str(a))
b=10.5
print(str(b))
c=10+2j
print(str(c))
print(str(True))    # bool True is convert to string
