# Write a program which accepts one number and checks whether it is divisible by 3 and 5

# Input: 15
# Output: Divisible by 3 and 5

def CheckDiv(No):
  if(No % 3 == 0 and No % 5 == 0):
    print("Divisible by 3 and 5")
  else:
    print("Not divisible by 3 and 5")

def main():
  Value = int(input("Enter number: "))

  CheckDiv(Value)
  

if __name__ == "__main__":
  main()