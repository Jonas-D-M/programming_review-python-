def try_convert(astring):
    try:
        int(astring)
        return True
    except ValueError:
        return False


def count_small_words(astring):
    counter_words = 0
    counter_chars = 0
    for i in astring.split():
        if not try_convert(i):
            for char in i:
                counter_chars += 1
            if counter_chars < 4:
                counter_words += 1
            counter_chars = 0
    return counter_words

astring = 'een string met daar in  kleine woorden'


def count_numbers(astring):
    counter = 0
    for i in astring.split():
        if try_convert(i):
            counter += 1
    if counter > 0:
        return counter
    else:
        return 'There where no numbers in this string.'

print(count_small_words(astring))
print(count_numbers(astring))
