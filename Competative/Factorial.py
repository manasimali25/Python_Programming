# Write a program which accepts one number and prints factorial of that number.

# Input: 5
# Output: 120

def Fact(No):
  Ans = 1

  for i in range(1, No+1):
    Ans = Ans * i
  return Ans

def main():
  Value = int(input("Enter number: "))

  Ret = Fact(Value)
  print("Factorial is: ",Ret)

if __name__ == "__main__":
  main()