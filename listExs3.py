# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
#
# Examples
# stutter("incredible") ➞ "in... in... incredible?"
#
# stutter("enthusiastic") ➞ "en... en... enthusiastic?"
#
# stutter("outstanding") ➞ "ou... ou... outstanding?"
# Notes
# Assume all input is in lower case and at least two characters long.

def stutter(s):
    return (s[0:2]+"... "+s[0:2]+"... "+s+"?")


# Write a function that converts hours into seconds.
#
# Examples
# how_many_seconds(2) ➞ 7200
#
# how_many_seconds(10) ➞ 36000
#
# how_many_seconds(24) ➞ 86400
# Notes
# 60 seconds in a minute, 60 minutes in an hour
# Don't forget to return your answer.

def how_many_seconds(n):
    return n * 3600


# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
#
# Examples
# radians_to_degrees(1) ➞ 57.3
#
# radians_to_degrees(20) ➞ 1145.9
#
# radians_to_degrees(50) ➞ 2864.8
# Notes
# The number π can be loaded from the math module with from math import pi.

def radians_to_degrees(n):
    return round(n * 57.295779513, 1)


# Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
#
# Examples
# factorial(3) ➞ 6
#
# factorial(5) ➞ 120
#
# factorial(13) ➞ 6227020800
# Notes
# Assume all inputs are greater than or equal to 0.
def factorial(n):
    total = 1
    for x in range(n, 0, -1):
        total = total * x
    return total


# Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
#
# Examples
# dis(1500, 50) ➞ 750
#
# dis(89, 20) ➞ 71.2
#
# dis(100, 75) ➞ 25
# Notes
# Your answer should be rounded to two decimal places.

def dis(p, d):
    return round(p - p * d / 100 , 2)


# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
#
# Person	    Relation
# Darth Vader	father
# Leia	        sister
# Han	        brother in law
# R2D2	        droid
# Examples
# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
#
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
#
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."

def relation_to_luke(s):
    lista = [
    "Darth Vader", "Luke, I am your father.",
    "Leia"	     , "Luke, I am your sister.",
    "Han"	     , "Luke, I am your brother in law.",
    "R2D2"	     , "Luke, I am your droid."]
    for x in range(0, 8, 2):
        if lista[x] ==  s:
            return lista[x+1]


# Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
#
# Examples
# Given that:
#   - "A" char code is: 65
#   - "a" char code is: 97
#
# counterpartCharCode("A") ➞ 97
#
# counterpartCharCode("a") ➞ 65
# Notes
# The argument will always be a single character.
# Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.

def counterpartCharCode(s):
    if s.islower():
        return ord(s.upper())
    elif s.isupper():
        return ord(s.lower())
    else:
        return ord(s)


# Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
#
# Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
#
# Examples
# binary(1) ➞ "1"
# # 1*1 = 1
#
# binary(5) ➞ "101"
# # 1*1 + 1*4 = 5
#
# binary(10) ➞ "1010"
# # 1*2 + 1*8 = 10
# Notes
# Numbers will always be below 1024 (not including 1024).
# The strings will always go to the length at which the most left bit's value gets bigger than the number in decimal.
# If a binary conversion for 0 is attempted, return "0".

def binary(n):
    return (str("{0:#b}".format(n))[2:])


# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
#
# Examples
# time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True
#
# time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False
#
# time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True
# Notes
# All test cases contain valid dates.

def time_for_milk_and_cookies(data):
    return True if (str(data)[-5:]) == "12-24" else False


# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
#
# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
#
# Examples
# is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

# is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

# is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29

def is_curzon(n):
    tot = 2 ** n + 1
    tot2 = 2 * n + 1
    return True if tot % tot2 == 0 else False


# Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
#
# Examples
# card_hide("1234123456785678") ➞ "************5678"
#
# card_hide("8754456321113213") ➞ "************3213"
#
# card_hide("35123413355523") ➞ "**********5523"
# Examples
# Ensure you return a string.
# The length of the string must remain the same as the input.

def card_hide(n):
    return ((len(n)-4) * "*") + (n[-4:])


# Create a function that replaces all the vowels in a string with a specified character.
#
# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
#
# replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
#
# replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"

def replace_vowels(s, c):
    vowels = ["a", "e", "i", "o", "u"]
    for x in vowels:
        s = s.replace(x, c)
    return s


# Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.
#
# Examples
# count_ones(0) ➞ 0
#
# count_ones(100) ➞ 3
#
# count_ones(999) ➞ 8

def count_ones(n):
    s = (str("{0:#b}".format(n))[2:])
    return s.count("1")


# Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
#
# Examples
# mood_today("happy") ➞ "Today, I am feeling happy"
#
# mood_today("sad") ➞ "Today, I am feeling sad"
#
# mood_today() ➞ "Today, I am feeling neutral"

def mood_today(s = "neutral"):
    return "Today, I am feeling "+s
