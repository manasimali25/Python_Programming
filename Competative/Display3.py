def Display(No):
  print("Inside Display")
  return No

def main():
  Value = 10
  Ret = Display(Value)
  print("Number is: ",Ret)

if __name__ == "__main__":
  main()