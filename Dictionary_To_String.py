x={'a':0,
   'b':1,
   'c':2,
   'd':3
  }

#convert x as y='abcd' and z='0123'


z=''.join([str(i) for i in x.values()])
y=''.join([i for i in x.keys()])

print(y)
print(z)