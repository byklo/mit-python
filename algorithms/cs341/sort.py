import random

def pickpivot(n):
	return random.randrange(n)

def partition(a, k, l, r):
# a [ l          k     r ]
	pivot_index = l
	swap(a, l, k)
	l += 1
	while (l <= r):
		if a[l] <= a[pivot_index]:
			l += 1
			continue
		if a[r] > a[pivot_index]:
			r -= 1
			continue
		swap(a, l, r)
	swap(a, pivot_index, r)
	return r

def quicksort(a, l, r):
	if l < r:
		pivot_index = pickpivot(r - l + 1) + l
		sorted_index = partition(a, pivot_index, l, r)
		quicksort(a, l, sorted_index - 1)
		quicksort(a, sorted_index + 1, r)

def swap(a, x, y):
	temp = a[x]
	a[x] = a[y]
	a[y] = temp

n = 10
a = random.sample(xrange(5*n), n)
print a

quicksort(a, 0, n-1)
print a
