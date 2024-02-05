import sys

letters = sys.argv[1]

print("\n"+"-"*len(letters)*4)

for x in range(0,len(letters)):
  print("| ",end="")
  for y in range(0,len(letters)):
      print(letters[y],end=" | ")
  letters=letters[1:]+letters[0]
  print("\n"+"-"*len(letters)*4)
