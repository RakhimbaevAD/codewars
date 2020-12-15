def song_decoder(song):
    original = list()
    for i in song.split(sep='WUB'):
        if i != '':
            original.append(i)
    return ' '.join(original)