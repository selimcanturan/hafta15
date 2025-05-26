
a1 = {'Ali':"baskan", 'Bugra':"yardimci", 'Ceyhun':"yardimci", 'Deniz':"yardimci", 'Elif': "baskan", 'Ferdi': "baskan"}


def buildReverse(dictionary):
    reverse = { }
    for key,value in dictionary.items():
        if value in reverse:
         reverse[value].append(key)
        else:
            reverse[value] = [key]
    return reverse

print(buildReverse(a1))