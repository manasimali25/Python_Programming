# Question: Write a program that accept two numbers from user and prints their addition, subtraction, multiplication, division

def Addition(No1, No2):

  Ans = 0
  Ans = No1 + No2
  return Ans

def Subtraction(No1, No2):

  Ans = 0
  Ans = No1 - No2
  return Ans

def Multiplication(No1, No2):

  Ans = 0
  Ans = No1 * No2
  return Ans

def Division(No1, No2):

  Ans = 0
  Ans = No1 / No2
  return Ans

def main():
  Value1 = int(input("Enter first number: "))
  Value2 = int(input("Enter second numbr: "))

  Ret = Addition(Value1, Value2)
  print("Addition is: ",Ret)

  Ret = Subtraction(Value1, Value2)
  print("Subtraction is: ",Ret)

  Ret = Multiplication(Value1, Value2)
  print("Multiplication is: ",Ret)

  Ret = Division(Value1, Value2)
  print("Division is: ",Ret)

if __name__ == "__main__":
  main()