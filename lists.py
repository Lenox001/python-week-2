my_list=[]
new_list=[10,20,30,40]
for element in new_list:
    my_list.append(element)
my_list.insert(2,15)
another_list=[50,60,70]
my_list.extend(another_list)
my_list.pop()
my_list.sort()
print(my_list.index(30))
print(my_list)
