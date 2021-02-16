
lst=[1,2,3,4,5,6]

m=[lst [x:x+2] for x in range(0,len(lst),2)]

print(m)


lst1=[[1,2],[3,4],[5,6]]

l=[]

for i in lst1:
    for j in i:
        l.append(j)

print(l)
