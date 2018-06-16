classmates = ['a0','b','c']
print(classmates, len(classmates) )
print( len(classmates))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[1][1], L[0][0])
for l in L:
	if(len(l) > 2):
		print(l)
	else:
		print(None)
		
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#for it, v  in d.items():
#	print(it , v )
#for v2 in d.values():
#	print(v2)
d["cc"] = 33
c = (1,2,3)
d[c] = 5

print([x*x for x in range(1,11) if x%2 == 0])
print([m+n for m in "DAVID" for n in "PAY"])

seek = set(c)
print(seek)
print(d.get('Bob'))
print(d)

def my_abs(x):
	if not isinstance(x,(int, float)):
		pass
		raise TypeError("bad operand type")
	if x >=0 :
		return x
	else :
		return -x
		
print(my_abs(-100))
#print(my_abs("aaa"))

#
def cals(*numbers):
	sum = 0 
	for n in numbers:
		sum = sum + n* n
	return sum
	
test_num = [1,2,3]

print(cals(*test_num))

def hanota(n,a,b,c) :
	if n==1 :
		print(a," --> ",c)
	else :
		#print(a," --> ",b)
		hanota(n-1 , a, c, b)
		hanota(1   , a, b, c)
		hanota(n-1 , b, a, c)
		

hanota(2, 'A', 'B', 'C')

def YH_triangles(max):
	n, L = 1, [[1]] 
	while n <= max:
		yield L
		inner_n, L_n = 0,[ ]
		while inner_n <= n:
			if(inner_n == 0 or inner_n == n):
				#b[inner_n],b[n] = 1,1
				L_n.append(1)
			else:
				L_n.append(L[n-1][inner_n] + L[n-1][inner_n-1])
			inner_n = inner_n + 1
		L.append(L_n)
		n = n + 1
	return 'done'

fYH = YH_triangles(9)
fYH
for n in fYH:
	print(n)
		
		
#map reduce
print("mapreduce")
def f(x):
	return x * x
map1 = map(f,[1,2,3,4,5,6])
print(map1)

def log(func):
	def wrapper(*arg, **kw):
		print("call %s()"%func.__name__)
		return func(*arg, **kw)
	return wrapper

@log
def now():
	print('2017')
	
now()

'a test module'

__author__ = 'David Pay'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello World')
	elif len(args) == 2:
		print('Hello, %s!' %args[1])
	else:
		print("Too many arguments")
		
if __name__=='__main__':
	test()
#name = input()
#print(name)
#print("h,w")