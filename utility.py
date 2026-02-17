word = input("Enter a word: ")

def uppercase(word):
  return word.upper()

def lowercase(word):
  return word.lower()

def capitalize(word):
  return word.capitalize()

upper = uppercase(word)
lower = lowercase(word)
capitalized = capitalize(word)
print("Uppercase version:", upper)
print("Lowercase version:", lower)
print("Capitalized version:", capitalized)