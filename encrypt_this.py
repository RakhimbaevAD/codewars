def encrypt_this(text):
    words_list = text.split(' ')
    res = list()
    for word in words_list:
        if len(word) != 0:
            word = list(word)
            word[0] = str(ord(word[0]))
            if len(word) > 2:
                word[1], word[-1] = word[-1], word[1]
            res.append(''.join(word))
    return ' '.join(res)