# Write a program which accepts length and width of rectangle and prints area.

def CalculateArea(Length, Width):
  Ans = 0
  Ans = Length * Width
  return Ans
  

def main():
  Value1 = int(input("Enter length: "))
  Value2 = int(input("Enter width: "))

  Ret = CalculateArea(Value1, Value2)
  print("Area of rectangle is: ",Ret)

if __name__ == "__main__":
  main()