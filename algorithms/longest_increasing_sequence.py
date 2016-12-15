import random

def lisLength(a):
	n = len(a)
	lis = [ 0 for i in xrange(n) ]
	lis[0] = 1

	for i in xrange(1, n):
		cur = 0
		for j in xrange(i):
			if a[j] < a[i] and cur < lis[j]:
				cur = lis[j]
		lis[i] = cur + 1

	return max(lis)

def lis(a):
	n = len(a)
	lis_len = [ 0 for i in xrange(n) ]
	lis_len[0] = 1
	lis = [ [] for i in xrange(n) ]
	lis[0] = [ a[0] ]
	max_i = 0
	max_len = 1

	for i in xrange(1, n):
		cur = 0
		lis[i] = [ a[i] ]
		for j in xrange(i):
			if a[j] < a[i] and cur < lis_len[j]:
				cur = lis_len[j]
				lis[i] = lis[j] + [ a[i] ]
		lis_len[i] = cur + 1
		if lis_len[i] > max_len:
			max_len = lis_len[i]
			max_i = i
	return lis[max_i]

a = random.sample(xrange(20), 10)

print a
print lisLength(a)
print lis(a)