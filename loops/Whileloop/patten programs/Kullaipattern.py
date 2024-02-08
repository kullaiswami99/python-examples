#str1='kullai'
print_K=[[' 'for i in range(6)]for j in range(6)]
print_U=[[' 'for i in range(6)]for j in range(6)]
print_L=[[' 'for i in range(6)]for j in range(6)]
print_L=[[' 'for i in range(6)]for j in range(6)]
print_A=[[' 'for i in range(6)]for j in range(6)]
print_I=[[' 'for i in range(6)]for j in range(6)]

# code for k a=row ,b=column
for a in range(6):
    for b in range(6):
        if(b==2 or a==b and b>=3 or a+b==6 and b>=2):
            print_K[a][b]='*'

# code for u a=row ,b=column
for a in range(6):
    for b in range(6):
        if(b==0 or a==5 or b==5):
            print_U[a][b]='*'

# code for l a=row ,b=column
for a in range(6):
    for b in range(6):
        if(b==0 or a==5):
            print_L[a][b]='*'

# code for l a=row ,b=column
for a in range(6):
    for b in range(6):
        if(b==0 or a==5):
            print_L[a][b]='*'

# code for a a=row ,b=column
for a in range(6):
    for b in range(6):
        if(a==0 or b==0 or a==3 or b==5):
            print_A[a][b]='*'

# code for i a=row ,b=column
for a in range(6):
    for b in range(6):
        if(a==0 or b==2 or a==5):
            print_I[a][b]='*'


for i in range(6):
    for j in range(6):
        print(print_K[i][j], end=' ')
    print(end='   ')
    for j in range(6):
        print(print_U[i][j], end='  ')
    print(end='   ')
    for j in range(6):
        print(print_L[i][j], end='  ')
    print(end='   ')
    for j in range(6):
        print(print_L[i][j], end='  ')
    print(end='   ')
    for j in range(6):
        print(print_A[i][j], end='  ')
    print(end='   ')
    for j in range(6):
        print(print_I[i][j], end='  ')
    print( )
