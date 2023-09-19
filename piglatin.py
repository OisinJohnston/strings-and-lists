

def translate(word):
    word = word.lower()
    if word[0] in 'aeiou':
        return word + 'way'
    first_char = word[0]
    word = word.replace(first_char, '', 1)
    return word + first_char + 'ay'
    
word = input("Enter the word too be translated: ")
print(f'translated word : {translate(word)}')



