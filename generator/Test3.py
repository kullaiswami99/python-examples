def fun(num):
    for i in range(1,11):
        return f'{num}X{i}={num*i}'
obj=fun(6)
for j in obj:
    print(j)