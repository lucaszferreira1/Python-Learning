from random import randint

# Challenge
# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
#
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(s):
    listaCapital = []
    for x in range(len(s)):
        if s[x].isupper():
            listaCapital.append(x)
    return listaCapital


# Write a function named mid that takes a string as its parameter.
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.
#
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(s):
    t = len(s)
    if t % 2 == 0:
        return ""
    else:
        t = int(t / 2)
        return s[t]


# Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
#
# For example, consider the following dictionary:
#
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
#
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
#
# Your function should return the number of people who are online.

def online_count(dic):
    o = 0
    for x in dic:
        if dic[x] == "online":
            o += 1
    return o


# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
#
# Calling the function multiple times should (usually) return different numbers.
#
# For example, calling random_number() some times might first return 42, then 63, then 1.

def random_number():
    return randint(1, 100)


# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
#
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False
def only_ints(x, y):
    return True if type(x) is int and type(y) is int else False


# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
#
# Define a function named double_letters that takes a single parameter.
# The parameter is a string.
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(s):
    for x in range(len(s)):
        oldLetter = s[x-1]
        if s[x] == s[x-1]:
            return True
            break
    return False


# Write a function named add_dots that takes a string and adds "." in between each letter.
# For example, calling add_dots("test") should return the string "t.e.s.t".
#
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
# For example, calling remove_dots("t.e.s.t") should return "test".
#
# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
#
# (You may assume that the input to add_dots does not itself contain any dots.)

def add_dots(s):
    stringRetorna = ""
    t = len(s)
    for x in range(t - 1):
            stringRetorna += s[x] + "."
    stringRetorna += s[t-1]
    return stringRetorna[:-1]

def remove_dots(s):
    return s.replace(".", "")


# Define a function named count that takes a single parameter. The parameter is a string.
# The string will contain a single word divided into syllables by hyphens, such as these:
#
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
#
# For example, the call count("ho-tel") should return 2.

def count(s):
    return s.count("-") + 1


# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(s1, s2):
    return True if sorted(s1) == sorted(s2) else False


# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
#
# Name your function flatten. It should take a single parameter and return a list.
#
# For example, calling:
#
# flatten([[1, 2], [3, 4]])
# Should return the list:
#
# [1, 2, 3, 4]

def flatten(l):
    lfinal = []
    for x in l:
        lfinal.extend(x)
    return lfinal


# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
#
# Your function should compute and return the difference between the largest and smallest number in the list.
#
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
#
# You may assume that no numbers are smaller or larger than -100 and 100.

def largest_difference(x):
    return max(x) - min(x)


# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
#
# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

def div_3(n):
    return n % 3 == 0


# Tic tac toe input
# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:
#
# 1:  X | O | X
#    -----------
# 2:    |   |
#    -----------
# 3:  O |   |
#
#     A   B  C
# The board is represented as a 2D list:
#
# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]
# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board.
# To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
#
# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column).
# Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
#
# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.

def get_row_col(i):
    i = list(i.strip(" "))
    i[1] = int(i[1])
    print(i)
    if i[0] == "A":
        boa = [i[1] - 1, 0]
    elif i[0] == "B":
        boa = [i[1] - 1, 1]
    elif i[0] == "C":
        boa = [i[1] - 1, 2]
    return (boa[0], boa[1])


# Palindrome
# A string is a palindrome when it is the same when read backwards.
#
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
#
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(s):
    scontrario = ""
    for let in range(len(s) - 1, -1, -1):
        scontrario += s[let]
    return True if s == scontrario else False


# Up and down
# Define a function named up_down that takes a single number as its parameter.
# Your function return a tuple containing two numbers;
# the first should be one lower than the parameter, and the second should be one higher.
#
# For example, calling up_down(5) should return (4, 6).

def up_down(n):
    return (n-1, n+1)


# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
# Your code should find the biggest number of consecutive zeros in the string.
# For example, given the string:
#
# "1001101000110"
# The biggest number of consecutive zeros is 3.
#
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
# Your function should return the number described above.

def consecutive_zeros(s):
    nxzero = 0
    n = 0
    for x in s:
        if x == "0":
            n += 1
            if n > nxzero:
                nxzero = n
        else:
            n = 0
    return nxzero


# All equal
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
#
# For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(l):
    if len(l) != 0:
        ant = l[0]
        for x in l:
            if x == ant:
                certo = True
                ant = x
            else:
                certo = False
                break
        return certo
    else:
        return True


# Boolean and
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(a, b, c):
    return True if a == b == c else False

# Writing short code
# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.
#
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
#
# What makes this tricky is that your function body must only contain a single line of code.

def convert(ns): return list(map(str, ns))


# Custom zip
# The built-in zip function "zips" two lists. Write your own implementation of this function.
#
# Define a function named zap. The function takes two parameters, a and b. These are lists.
#
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
#
# You may assume a and b have equal lengths.
#
# If you don't get it, think of a zipper.
#
# For example:
#
# zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# )
# Should return:
#
# [(0, 5),
#  (1, 6),
#  (2, 7),
#  (3, 8)]

def zap(a, b):
    maior = a if a >= b else b
    for x in maior:
        na = a[x]
        nb = b[x]
        final[x] = (na, nb)
    return final

print( zap([0, 1, 2, 3],[5, 6, 7, 8]))
