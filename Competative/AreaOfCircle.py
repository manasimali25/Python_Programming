# Write a program which accepts radius of circle and prints area of circle.

def CalculateArea(Radius):
  Pi = 3.14
  Ans = Pi * Radius * Radius
  return Ans
  

def main():
  Value = int(input("Enter Radius: "))

  Ret = CalculateArea(Value)
  print("Area of circle is: ",Ret)

if __name__ == "__main__":
  main()