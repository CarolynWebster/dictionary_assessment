"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # make a set of only the unique words
    # unique_words = set(words)
    # convert that set into a list
    # list_of_unique_words = list(unique_words)

    #return list_of_unique_words

    #turn words into a set and then turn that set into a list to be returned
    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    
    #make sets of the two lists to reduce them to only unique items
    unique_items1 = set(items1)
    unique_items2 = set(items2)

    #use set math to compare the two sets and return as a list
    return list(unique_items1 & unique_items2)

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    
    # Make an empty list to hold the pairs
    zero_sum_pairs = []
    # make a copy of the numbers list so we don't change the original input
    # using set to eliminate any duplicate numbers and then convert back to list
    numbers_sorted = list(set(numbers[:]))
    # sort the list
    numbers_sorted.sort()
    # loop through the numbers in the copy of the list
    for num in numbers_sorted:
        # if the inverse of that number is in the list
        if -num in numbers:
            # get the index of the matching inverse number
            neg_num_index = numbers_sorted.index(-num)
            # put the matching pair of numbers together
            pair = [numbers_sorted[neg_num_index], num]
            # we use the negative numbers first
            # then break once we go over zero bc all pairs will have been created
            if num <= 0:
                #add the pair to the list
                zero_sum_pairs.append(pair)
            else:
                break


    #return the list of pairs
    return zero_sum_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # make a blank dictionary
    word_count = {}

    #strip out all space characters so we just have letters/punctuation
    no_space_phrase = phrase.replace(" ", "")

    # convert to lowercase so all letters are evaluated the same
    no_space_phrase = no_space_phrase.lower()

    # iterate over the list building counts and putting them in a dictionary
    for letter in no_space_phrase:
        # look in the dictionary, if the letter is in there already
        # return the count value associated with the letter and add 1
        # if it isn't a new key is made starting at 1
        word_count[letter] = word_count.get(letter, 0) + 1

    #return a list of key, value tuples so we can sort them
    count_list = list(word_count.items())

    # We covered this in the diving deeper study hall and I wanted to try it out
    # order the list by second index by redefining how things are compared
    # count_list.sort(cmp=lambda x, y: cmp(x[1], y[1]), reverse=True)

    # make list to hold the most used letters
    # most_used_letters = []

    # for count in count_list:
    #     # if the count matches the highest count, add it to the list
    #     # this will add the first by default bc of course it will match itself
    #     # count([0] = letter, [1] = count)
    #     if count[1] == count_list[0][1]:
    #         most_used_letters.append(count[0])
    #     else:
    #         #stop looping once we no longer have matching counts
    #         break

    # return most_used_letters

    # another way would be to invert the tuples so the numbers were first
    # so we could use a more traditional sort
    for i in range(len(count_list)):
        # rebinding tuple as (count, letter)
        count_list[i] = (count_list[i][1], count_list[i][0])

    count_list.sort(reverse=True)

    most_used_letters = []
    for count in count_list:
        # if the count matches the highest count, add it to the list
        # this will add the first by default bc of course it will match itself
        # count([0] = count, [1] = letter)
        if count[0] == count_list[0][0]:
            most_used_letters.append(count[1])
        else:
            #stop looping once we no longer have matching counts
            break

    #sort the list to be alphabetical
    most_used_letters.sort()

    #return the sorted list of most used letter(s)
    return most_used_letters

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
