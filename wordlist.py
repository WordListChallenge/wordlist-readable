import fileinput

# Find all ways to write a word of length 6
# as a concatenation of two shorter words from the same dictionary.

dictionary_file = "testdata/wordlist_utf8.txt"
target_length = 6
fragments = set()


def init_fragments():
    """
    Initialize the fragments set.
    After this method finishes, the fragments set will contain
    all dictionary words of length 5 or less.
    """
    for word in fileinput.input(dictionary_file):
        word = word.strip()
        if len(word) < target_length:
            fragments.add(word)


def check(word):
    """
    Check if the input word is composed of two shorter words.
    Print the compositions, if any.
    """
    for i in range(1, target_length):
        if word[0:i] in fragments and word[i:] in fragments:
            print("%s + %s => %s" % (word[0:i], word[i:], word))


#################
# Program start #
#################
init_fragments()

for w in fileinput.input(dictionary_file):
    w = w.strip()
    if len(w) == target_length:
        check(w)
