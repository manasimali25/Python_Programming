def main():
  Value = input("Enter input: ")
  print("Datatype is: ",type(Value))
  print("Memory address is: ",id(Value))
  print("Size is: ",Value.__sizeof__())


if __name__ == "__main__":
  main()