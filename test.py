# fruit_list1=['Apple','Banana','Cherry','Date','Elderberry']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Apricot'
# fruit_list3[1]='Blueberry'
# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0]=='Apricot':
#         sum+=1
#     if ls[1]=='Blueberry':
#         sum+=20
# print(sum)

# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     return values
# f(1)
# f(2)    
# f(3)

# def f(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# f(t,v)
# print(t,v[0])

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

fruit={}
def adddone(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
adddone('Apple')
adddone('Banana')   
adddone('apple')
print(len(fruit))