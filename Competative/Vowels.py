# Write a program which accepts one character and checks whether it is vowel or consonant.

# Input: a
# Output: Vowel

def ChkVowel(Char):

  if(Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u'):
    print(f"{Char} is Vowel")
  else:
    print(f"{Char} is Consonant")

def main():
  Value = input("Enter character: ")

  ChkVowel(Value)

if __name__ == "__main__":
  main()