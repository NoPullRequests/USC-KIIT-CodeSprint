text = input()
processed_text = text.lower()

vowels = 0
consonants = 0

for char in processed_text:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

words_list = text.split()
word_count = len(words_list)

print(vowels)
print(consonants)
print(word_count)
