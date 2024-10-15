''' int data type '''
a=10        # decimal form
b=0b101010  # binary form
c=0o12345   # octal form
d=0xBeef    # hex form
print(a)
print(b)
print(c)
print(d)

''' Base conversion '''
print(bin(a))
print(oct(b))
print(hex(c))
print(d)

''' float '''
e=2e3               # 2 * 10^3
print(type(e))
print(e)


''' complex '''
a=2+5j
b=2+2J
c=0b1010+2j         # but cant c=2+0b101010j
print(type(a))
print(a)
print(b)
print(c)
print("real=",a.real,'and imag=',a.imag)


''' bool '''

a=True
b=False
print(type(a))
print(a)
print(b)
c=10
d=20
e=c>d
print(e)
f=True
g=True
print(f+g)          # True->1 and False ->0

''' str '''
a='A'
b='Aayush'
print(type(a))
print(type(b))
c='''
My
name
is
Aayush
'''
print(type(c))
print(c)

d='abcd'
print(d[1])
print(d[-3])
print(d[:-1])

e="#"*10
print(e)

f='hello'
print(f[0].upper()+f[1:])
print(f[:-1]+f[-1].upper())
a='aayush'
print(a[::-1])