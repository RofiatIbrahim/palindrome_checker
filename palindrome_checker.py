word = input("Enter the word: ") 
word = word.lower() 
reversed_word = word[::-1] 
reversed_word = reversed_word.lower() 
if word == reversed_word: 
  print(f"{word} is a palindrome") 
else: 
  print(f"{word} is not a palindrome")