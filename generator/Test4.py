def fun(num):
    my_list=[]
    for i in range(1,11):
        my_list.append(f'{num}X{i}={num*i}')
    return my_list
       
obj=fun(6)
for j in obj:
    print(j)  