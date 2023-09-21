"""
    File: rhymes.py
    Author: Hengsocheat Pok
    Purpose: finding perfect rhymes of a word given by the user.
"""

def read_dict_file (filename):
    """
    This will read the main txt dictionary file and return a dictionary that
    maps each word to a list of its own phonemes.

    :param: filename: the main dictionary file of words and associated phonemes

    :return: a new dictionary mapping the words to their list of phonemes

    pre-condition: filename is a dictionary

    post-condition: a dictionary returned
    """
    dict = {}                                           # a new and empty dictionary
    lines = [] # a new and empty list
    with open (filename, 'r') as dict_file:             # begin reading the file
        for l in dict_file:                             # accessing each and every  line in the file
            lines.append(list(l.split()))               # the empty list appends the words and associated phonemes line by line
    for line in lines:
        if line[0] not in dict:                         # to prevent repetition of the same word from happening
            dict[line[0]] = []
        dict[line[0]].append(list(line[1: ]))
    return dict                                         # a dictionary in the form of keys mapped to values that are list of lists of elements (phonemes)


def primary_stress_search (phonemes, word_analyzed):
    """
    This function will analyze a word from the input by user and then find the phonemes associated in the main
    dictionary and create and return a new dictionary with information about pronunciation.

    :param: phonemes: the dictionary created by the previous function. We will call it the main dictionary from this point on.

    :param: word_analyzed: typed in by the user. It will be analyzed and used to find its rhyme members by creating another dictionary out of it.

    :return: a dictionary of the word being analyzed with phonemes in it, phonemes of the word analyzed.

    """
    l = []                                                                  # an empty list
    for k in phonemes:                                                      # these phonemes refer to the ones in the dictionary previously created
        v = phonemes[k]
        if k == word_analyzed.upper():                                      # forcing the word being analyzed to be upper-cased
            for list_of_lists in range (len(v)):                            # the top level lists of the values
                for phoneme in range (len(v[list_of_lists])):               # the inner lists of the values
                        if '1' in v[list_of_lists][phoneme]:                # detecting the primary stressed phonemes
                            l.append (v[list_of_lists][phoneme - 1])        # append the phoneme before the primary stress
                            l.append (v[list_of_lists][phoneme:])           # append the primary stress and the phonemes after
    analysis = []                                                           # an empty list soon-to-be used
    new_d = {}                                                              # a dictionary for soon-to-be used
    for element in (l):                                                     # accessing the elements of l
        analysis.append(element)                                            # appends the elements
    for el in range (0, len(analysis) - 1, 2):                              # each step of the iteration is 2, so the minus one part is to prevent indexing out of range
        if analysis[el] not in new_d:                                       # to prevent redundancy
            new_d[analysis[el]] = []
            new_d[analysis[el]].append(analysis[el + 1])
        else:
            new_d[analysis[el]].append(analysis[el + 1])
    return new_d                                                            # the new dictionary here will be in the form of phoneme prior the primary stress mapped to the a
                                                                            # list of lists of phonemes from the ones that are the primary stress to the end.

def linking_rhymes (main_dict, the_new_d):
    """
    This function will analyze the dictionary created previously (of the phonemes of the word being examined) and find its rhyme members in a list.

    :param main_dict: the main dictionary explained

    :param the_new_d: the dictionary of the word being examined, storing the associated phonemes.

    :return: a list of rhymes
    """

    rhymes_list = []                                                            # a new list for storing the rhymes
    for word in main_dict:                                                      # accessing the main dictionary
        phonemes_list = main_dict[word]
        for inner_phonemes_list in phonemes_list:
            for phoneme in range(len(inner_phonemes_list)):                     # phoneme refers to the individual phoneme inside the
                # main dictionary

                for key in the_new_d:                                           # accessing the new dictionary of the word whose rhymes we are searching for
                    value = the_new_d[key]
                    for  v in value:                                            # value refers to the new_dict's outside list and v, the inner one.

                        for pho in range(len(v)):                               # pho refers phonemes inside the v
                            if inner_phonemes_list[phoneme: ] == v:             # making sure that the primary stress and the subsequent phonemes in both words being compared are identical
                                if inner_phonemes_list[phoneme - 1] == key:     # checking if the phonemes prior the stress phonemes of the two words are identical
                                    pass
                                else:
                                    rhymes_list.append(word)
                                    break                                       # to avoid redundancy
    return sorted(rhymes_list)                                                  # alphabetically sorting the list returned


def main():
    """
    For reading the user inputs, a dictionary file and a word typed by the user. Also for executing all functions, making them work together.
    """
    pfile = "PronunciationDictionary.txt"
    word = input("Type in your word: ")
    print()
    dictionary_input = read_dict_file(pfile)
    primary_stress = primary_stress_search (dictionary_input, word)
    rhymes = linking_rhymes(dictionary_input, primary_stress)                   # this is the sorted version of the list of rhymes
    print(len(rhymes), " Results Found: \n")
    for i in range(len(rhymes)):                                                # rhymes is a list being indexed through
        print (i + 1, ": " + rhymes[i])                                         # print each rhyming word line by line and alphabetically

main()


