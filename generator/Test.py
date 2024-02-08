def fun(num):
    for i in range(1,11):
        yield f'{num}X{i}={num*i}'
obj=fun(6)
for value in obj:
    print(value)
