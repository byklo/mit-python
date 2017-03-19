# sorted permutations
# n = 4, k = 3
# Sn = [ 1, 2, 3, 4 ]
# generate all k-length permutations in sorted order
# 1, 2, 3
# 1, 2, 4
# 1, 3, 4
# 2, 3, 4

def sort_perm(a, k, pre):
	# print "a %s k %s pre %s" % (a, k, pre)
	if len(a) == k:
		pre += ''.join([ str(x) for x in a ])
		print pre
	elif k > -1:
		sort_perm(a[1:], k, str(pre))
		sort_perm(a[1:], k-1, str(pre) + str(a[0]))
	return

n = 6
k = 3

sort_perm(range(1, n + 1), k, "")