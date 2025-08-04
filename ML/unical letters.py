def count_inique_consonants(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    unique_consonants = set()
    
    for char in text.lower():
        if char.isalpha() and char not in vowels:
            unique_consonants.add(char)
                                  
    return len(unique_consonants)