a = []
for i in range(1,1000,1):
  if(i % 3 == 0 or i % 5 == 0):
    a.append(i)
d = 0
for n in a:
  d += n
print(d)  
