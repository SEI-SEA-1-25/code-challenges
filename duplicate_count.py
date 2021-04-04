# Count the number of Duplicates
# Write a function that will return 
# the count of distinct case-insensitive 
# alphabetic characters and numeric digits that 
# occur more than once in the input string. The input 
# string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.

String1 = "abcd" #0
String2 = "abbccd" #2 b's, & 2 c's
String3 = "aAbcdd" #2 a's (one uppercase), & 2 d's
String4 = "12334bb" #2 3's & 2 b's

def duplicate_count(text):
    doubles = {}
    text_l = text.lower()
    for i in text_l:
        if i in doubles:
            doubles[i] += 1
        else:
            doubles[i] = 1
    for key, value in doubles.items():
        if value > 1:
            print(key, end = " ")
    print()
    

duplicate_count(String4)