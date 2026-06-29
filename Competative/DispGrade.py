# Write a program which accepts marks and displays grade.

# Condition Example:
#  ≥ 75 → Distinction
# ≥ 60 → First Class
# ≥ 50 → Second Class
# < 50 → Fail

def DispGrade(No):
  if(No >= 75):
    print("Distinction")
  
  elif(No >= 60):
    print("First Class")

  elif(No >= 50):
    print("Second class")

  else:
    print("Fail")

    
def main():
  Marks = int(input("Enter marks: "))

  DispGrade(Marks)

if __name__ == "__main__":
  main()