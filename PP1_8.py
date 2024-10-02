
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
  print(bool3 > 0 and bool3 < 10)

def q4():
  bool4 = input("Input food: ")
  bool5 = input("Input drink: ")
  if bool4 == "Pizza" or "pizza" and bool5 == "pop" or "Pop" :
    print(True)
  else :
    print(False)


def q5():
  print(int(input("Enter an integer: ")) % 2 == 0)
  
#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()