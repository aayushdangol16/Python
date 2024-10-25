# ''' int data type '''
# a=10        # decimal form
# b=0b101010  # binary form
# c=0o12345   # octal form
# d=0xBeef    # hex form
# print(a)
# print(b)
# print(c)
# print(d)

# ''' Base conversion '''
# print(bin(a))
# print(oct(b))
# print(hex(c))
# print(d)

# ''' float '''
# e=2e3               # 2 * 10^3
# print(type(e))
# print(e)


# ''' complex '''
# a=2+5j
# b=2+2J
# c=0b1010+2j         # but cant c=2+0b101010j
# print(type(a))
# print(a)
# print(b)
# print(c)
# print("real=",a.real,'and imag=',a.imag)


# ''' bool '''

# a=True
# b=False
# print(type(a))
# print(a)
# print(b)
# c=10
# d=20
# e=c>d
# print(e)
# f=True
# g=True
# print(f+g)          # True->1 and False ->0

# ''' str '''
# a='A'
# b='Aayush'
# print(type(a))
# print(type(b))
# c='''
# My
# name
# is
# Aayush
# '''
# print(type(c))
# print(c)

# d='abcd'
# print(d[1])
# print(d[-3])
# print(d[:-1])

# e="#"*10
# print(e)

# f='hello'
# print(f[0].upper()+f[1:])
# print(f[:-1]+f[-1].upper())
# a='aayush'
# print(a[::-1])

# ''' list '''
# a=[10,20,30,10,'ayush',True]
# print(a)
# print(type(a))
# print(a[1])
# print(a[0:4])
# a.append(40)
# a.append(10)    # append at last
# print(a)
# a.remove(10)    # if duplicate value remove agade ko value
# print(a)
# a[0]=100
# print(a)

# ''' tuples '''
# a=(1)           # it is int
# print(type(a))
# a=(1,)          # to create single element tuple 
# print(type(a))
# b=(1,2,1,2,3,4)
# print(b)
# print(b[2])
# print(b[0:4])

# ''' set '''
# s={1,2,3,4}
# print(type(s))
# q=set()             # empty set
# print(type(q))
# s={10,20,"aayush",10}
# print(s)
# s.add("Dangol")
# print(s)
# s.add(30)
# print(s)
# s.remove(30)
# print(s)

# ''' frozenset '''
# s={10,20,30.5,"Aayush",True}
# fs=frozenset(s)
# print(fs)
# print(type(fs))

# ''' dict '''
# d={}                # empty dict
# print(type(d))
# d={
#     100:"Aayush",
#     200:"Dangol"
# }
# print(d)
# d[300]="shatvik"
# print(d)
# d[100]="Aayush Dangol"
# print(d)
# d[400]=10
# print(d)

# ''' range '''
# r=range(10)
# for i in r:
#     print(i)
# r=range(10,20)
# for i in r:
#     print(i)
# r=range(10,20,2)
# for i in r:
#     print(i)

# r=range(20,10,-1)
# for i in r:
#     print(i)
# print()
# r=range(10)
# print(r[2])
# print(r[2:5])

# ''' bytes '''
# b=[10,20,30,40]
# by=bytes(b)
# print(by)
# print(by[0])
# print(by[0:2])

# ''' bytearray '''
# b=[10,20,30]
# by=bytearray(b)
# by.append(40)
# for i in by:
#     print(i)
# by.remove(40)
# by[0]=100
# for i in by:
#     print(i)

# ''' None '''
# a=None
# print(type(a))