#Write a Python program to count the number of characters (character frequency) in a string

def finder():
    x=input('enter a string')
    a=dict()
    for n in x: 
        if n in a.keys():
            a[n] += 1
        else:
             a[n] = 1
    print(a)


finder()




