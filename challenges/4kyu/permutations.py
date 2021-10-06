import itertools


def permutations(string):
    result = list()
    for i in itertools.permutations(string,len(string)):
        result.append(''.join(i))
    return set(result)