def threetimesxplusone(x):
    list=[x]
    while x!=1:
        x=x//2 if x%2==0 else 3*x+1
        list.append(x)
    return list

def timestable():
    for i in range(1, 9+1):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(j, i, i*j), end='')
        print()

print(threetimesxplusone(13))
mid=list(map(len,list(map(threetimesxplusone,range(2,100+1)))))
print(mid.index(max(mid))+2)

timestable()
