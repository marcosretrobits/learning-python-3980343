# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 10, 100
#print(x,y)

# conditional flow uses if, elif, else
if x < y:
  print("x < y")
elif x==y:
  print("=")
else:
  print("x > y")

# conditional statements let you use "a if C else b"
result = "x is less than y" if (x<y) else "x >= y"
print(result)
