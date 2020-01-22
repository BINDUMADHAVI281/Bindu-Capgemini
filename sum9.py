L=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    elements=int(input())
    L.append(elements)
print(L)
for n in L:
    print(n*'*')
