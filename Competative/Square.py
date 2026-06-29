# Write a program which accepts one number and prints square of that number.

# Input: 5
# Output: 25

def Square(No):
  Ans = No * No
  return Ans

def main():
  Value = int(input("Enter number: "))

  Ret = Square(Value)
  print("Square is: ",Ret)

if __name__ == "__main__":
  main()