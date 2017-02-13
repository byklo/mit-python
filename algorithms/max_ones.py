def count(a):
	prev = 0
	max_count = 0
	cur_count = 0
	for x in a + [0]:
		if x and prev:
			cur_count += 1
		elif x:
			cur_count = 1
			prev = 1
		elif prev:
			max_count = max(cur_count, max_count)
			cur_count = 0
			prev = 0
	return max_count

seqs = [
	[0,1,1,0,1,0,1,1,1,1,0,0,1],
	[1,1,1,1,1],
	[0,1,0,0,0],
	[1,0,0,0,0],
	[1,0,1,1,1]
]

for seq in seqs:
	print seq
	print count(seq)
