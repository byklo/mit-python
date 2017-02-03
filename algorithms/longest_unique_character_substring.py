# longest unique character substring

def lucs(string):
    # return length
    # 1 - asdf, return length of full string
    #     1234
    # 2 - asssdf,
    #     --x
    # cur 121123
    #     ----
    #    sssdfdfd
    #    asdfjjjj
    #    ssssssss
    #    sssfffff
    #    --122
    # max   22
    #    sdeffsdvb
    # maintaining a max
    # if i reach a repeated char, then update max
    # ssssss[s]
    max_length = 0
    cur_length = 0
    seen_chars = {}
    for i,x in enumerate(string):
        if seen_chars.has_key(x):
            # seen, repeated
            max_length = max(max_length, cur_length)
            cur_length = 0
            seen_chars = {}
        cur_length += 1
        seen_chars[x] = 1
    max_length = max(max_length, cur_length)
    return max_length

strings = [ "asdf", "asssdf", "sssdfdfdf", "ssssfffff", "asdfjjjjj", "sdeffsdvb" ]

for s in strings:
    print lucs(s)

# O(1) SPACE BECAUSE ASCII