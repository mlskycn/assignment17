sentence = input("Enter your sentence: ")

my_dict = {}

for letter in sentence:
    if letter != " ":
        my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)