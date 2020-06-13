def check_if_anagrams(word1,word2):
    firstSorted = sorted(word1)
    secondSorted = sorted(word2)

    if firstSorted == secondSorted:
        print("{:s} and {:s} are Anagrams".format(word1,word2))

    else:
        print("{:s} and {:s} are not Anagrams".format(word1,word2))

check_if_anagrams('iceman','cinema')