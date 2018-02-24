import string
import math

ta = "bu qədər asan ola bilməz ki"
tb = "Thinking on your own is good, , , , ,   when you solve the problems"


def lower(text):
    return text.lower()


def split(text):
    return text.split()


def remove_punct(text):
    return text.translate(text.maketrans(string.punctuation, " " * len(string.punctuation)))


def compare(texta, textb):
    texta = split(lower(remove_punct(texta)))
    textb = split(lower(remove_punct(textb)))

    general_set = set()
    for i in texta:
        general_set.add(i)
    for i in textb:
        general_set.add(i)
    print(general_set)

    map_a = {}
    map_b = {}
    for i in general_set:
        map_a[i] = 0
        map_b[i] = 0

    for i in texta:
        map_a[i] = map_a[i] + 1
    for i in textb:
        map_b[i] = map_b[i] + 1
    print(map_a)
    print(map_b)

    ab = 0
    a = 0
    b = 0
    for i in general_set:
        ab += map_a[i] * map_b[i]
    for i in general_set:
        a += map_a[i] ** 2
    for i in general_set:
        b += map_b[i] ** 2

    print(ab)
    print(math.sqrt(a))
    print(math.sqrt(b))
    cos = ab / (math.sqrt(a) * math.sqrt(b))
    print(cos)
    pass
#
# compare(ta, tb)
# print(split(lower(remove_punct(tb))))


stopwords = []

with open("../files/stop-words-AZ.txt", "r", encoding="utf8") as stopwords_file:
    for word in stopwords_file:
        stopwords.append(word.strip())


texta = split(lower(remove_punct(ta)))

print(stopwords)
for i in texta:
    if i in stopwords:
        texta.remove(i)
print(texta)



