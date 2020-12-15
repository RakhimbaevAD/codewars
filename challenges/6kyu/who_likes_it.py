def likes(names):
    if len(names) == 0:
        textToReturn = 'no one likes this'
    elif len(names) == 1:
        textToReturn = str(names[0]) + ' likes this'
    elif len(names) == 2:
        textToReturn = str(names[0]) + ' and ' + str(names[1]) + ' like this'
    elif len(names) == 3:
        textToReturn = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[-1]) + ' like this'
    else:
        textToReturn = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(len(names) - 2) + ' others like this'
    return textToReturn