# Write a program which accepts one number and prints multiplication table of that number.

# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40

def Multi(No):

  for i in range(1,11):
    Ans = No * i
    print(Ans)
    

def main():
  Value = int(input("Enter number: "))

  print("table of:",Value)
  Multi(Value)
  

if __name__ == "__main__":
  main()