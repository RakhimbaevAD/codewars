def find_outlier(integers):
    even = 0
    odd = 0
    for i in range(3):
        if integers[i]%2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        for j in integers:
            if j%2 != 0:
                return j
    else:
        for j in integers:
            if j%2 == 0:
                return j