def duplicate_count(text):
    exists_once = {}
    exists_twice = {}
    for letter in text.lower():
        if(letter in exists_once):
            exists_twice[letter] = True
        else:
            exists_once[letter] = True
            
    return(len(exists_twice))