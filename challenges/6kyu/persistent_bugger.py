def persistence(n):
    import numpy
    list_n = [int(i) for i in str(n)]
    if n < 10:
        return 0    
    n = numpy.prod(list_n)
    return 1 + persistence(n)