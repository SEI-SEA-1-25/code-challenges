# Write a function that will return the count of
# distinct case-insensitive alphabetic characters and
# numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only
# alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    # Your code goes here
    dup_count = 0
    text = text.lower()
    new_list = [i for i in text]
    dup_arr = [i for i in new_list if ]
    # dup_list = [i for i i]
    return new_list

    # list comprehension
    # turn it to string, lower case
    # if it matches itself, plus one to variable

# print([item for item, count in collections.Counter(a).items() if count > 1])

print(duplicate_count('indiviSible'))