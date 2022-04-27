#Find the mininum value

#Method 1 with for loop

a=[4,7,4,2,76,8,9,43,23,1,6,3,5,88,6,43,43]
b=None
for i in a:
  if b==None:
    b=i 
  elif b>i: 
    b=i
print(b)

#Method 2 with while loop

x=0
mini=None
while x<len(a):
    if mini==None:
        mini=a[x]
    elif mini>a[x]:
        mini=a[x]
    x+=1
print(mini)

#Method 3
m=min(a)
print(m)

