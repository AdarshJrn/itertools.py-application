import itertools

a = int(input())
given = list(map(int, input().split()))
l = list(map(int, input().split()))
maxit = []
for i in range(len(l)):
    maxit = maxit + [[j for j in range(0, l[i] + 1)]]
final = []
indes = []
combi = list(itertools.product(*maxit))
#combi.reverse()   # if you need least and also use almost all max values
for i in range(len(combi)):
    out = 0
    for j in range(len(given)):
        out = out + given[j] * combi[i][j]
    if(out == a):
        final.append(sum(combi[i]))
        indes.append(i)
if(len(indes) == 0):
    print('not found')
    exit()
print(combi[indes[final.index(min(final))]])
