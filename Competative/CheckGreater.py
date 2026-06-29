# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

# Input: 10 20
# Output: 20 is greater

def ChkGreater(No1, No2):
  if(No1 > No2):
    print("Greater number is: ",No1)
  elif(No2 > No1):
    print("Smaller number is: ",No2)
  else:
    print("Both are equal")

def main():
  Value1 = int(input("Enter first number: "))
  Value2 = int(input("Enter second number: "))

  ChkGreater(Value1, Value2)


if __name__ == "__main__":
  main()