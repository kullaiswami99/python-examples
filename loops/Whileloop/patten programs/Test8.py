'''list1=[1,2,3]
list2=[[i for i in  list1] for i in range(4)]
print(list2)'''

list2=[[i for i in  range(5)] for j in range(4)]
print(list2)
print(list2[3][4])
