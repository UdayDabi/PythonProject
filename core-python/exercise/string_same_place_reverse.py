name = "vijay dinanath chouhan"
word_list = name.split()  # ['vijay', 'dinanath', 'chouhan']

for word in word_list:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")


# str1 = input("Enter a string: ")
# count = 0

# for ch in str1:
#     if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#         count += 1

# print("Total vowels =", count)
