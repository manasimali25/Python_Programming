# Write a program which accepts one number and prints sum of first N natural numbers.

# Input: 5
# Output: 15

def Summation(No):
  Ans = 0

  for i in range(1, No+1):
    Ans = Ans + i
  return Ans

def main():
  Value = int(input("Enter number: "))

  Ret = Summation(Value)
  print("Summation is: ",Ret)

if __name__ == "__main__":
  main()