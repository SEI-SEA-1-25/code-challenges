def duplicate_count(text):
    # Your code goes here
    # arr = list(text) 
    count = {}
    lower_text = text.lower()
    duplicates = 0
    for letter in lower_text:
        if letter in count:
            count[letter] += 1
        else: 
            count[letter] = 1
    
    for key, value in count.items():
        if value > 1:
            duplicates += 1
    return duplicates
        
 




print(duplicate_count('Indivisibilities'))