str1='No'
print_N=[[' 'for i in range(6)]for j in range(6)]
print_O=[[' 'for i in range(6)]for j in range(6)]

# code for N a=row ,b=column
for a in range(6):
    for b in range(6):
        if(b==0 or a==b or b==5):
            print_N[a][b]='*'

# code for O a=row ,b=column
for a in range(6):
    for b in range(6):
        if(a==0 or a==5 or b==0 or b==5):
            print_O[a][b]='*'

for  i in range(6):
    for j in range(6):
        print(print_N[i][j],end=' ')
    print(end='  ')
    for j in range(6):
        print(print_O[i][j],end=' ')
    print()