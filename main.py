

f= open("test.txt")
result = ""
for line in f:
  new_line = line.rstrip()
  e = chr(int(new_line))
  #print(e)
  result = result + e
print(result)
f.close()


result =""
f= open("problem.txt")
for line in f:
  new_line = line.rstrip()
  e = chr(int(new_line))
  #print(e)
  result = result + e
print(result)

f.close()