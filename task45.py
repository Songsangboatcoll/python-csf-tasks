#45
user_name = input("Please enter your name: ")
vowel_count = 0

for char in user_name:
    if char.lower() in "aeiou":
        vowel_count += 1
print("The number of vowels in your name is: ", vowel_count)