s=input()
r=''
v="aeiou"
for p in s:
    if p in v:
        if p=='u':
            r=r+"a"
        else:
            r=r+v[v.index(p)+1]
    else:
        r=r+p
print(r)


    
