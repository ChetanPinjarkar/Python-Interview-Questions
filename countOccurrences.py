ls = ['a','a','b','c','c']
ls1=[]
dt = {}

for i in ls:
  if i not in ls1:
    dt.update({i:1})
    ls1.append(i)
  else:
    count = dt[i]+1
    dt.update({i:count})    
print(dt)
