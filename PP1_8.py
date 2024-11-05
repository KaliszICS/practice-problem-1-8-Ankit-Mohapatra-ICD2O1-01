
def q1():
   bool1 = True
   bool2 = False
   print(bool1 and bool2)
   print(bool1 or bool2)

def q2():
   x = int(input("Enter an integer: "))
   print(x != 0)

def q3():
   bool3 = int(input("Enter a number: "))
   print(bool3 >= 0 and bool3 <= 10)

def q4():
 x = input("Input food: ")
 y = input("Input drink: ")
 if x.lower() == "pizza" and y.lower() == "pop":
     print(False)
 else:
     print(True)


def q5():
  x = int(input("Enter an integer: "))
  print(f"The integer {x} is {(x % 2 == 0)}")

#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
