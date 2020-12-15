def find_it(seq):
    count = dict()
    for i in seq:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in count:
        if count[i]%2 != 0:
            return i