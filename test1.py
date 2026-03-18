#secret message question.Write an algorithm to count the number of special characters in a string. Special characters are defined as any character that is not a letter or a digit. 
#re module can be used to count the number of special characters in a string. Here is an example of how to do this:
# stri=input("Enter the string: ")
# def countspecial(stri):
#     sc=['@','#','$','%','^','&','*','(',')','-','+','!','?','/','<','>','|','~','_','`','=']
#     cou=0
#     for i in sc:
#         cou+=stri.count(i)
#     return cou
# print(countspecial(stri))

#Alternate solution using re module
# stri=input("Enter the string: ")
# import re
# def count_special_characters(s):
#     # Use regular expression to find all non-alphanumeric characters
#     special_characters = re.findall(r'[^a-zA-Z0-9]', s)
#     return len(special_characters)

# print(count_special_characters(stri))

# another solution using re module
# stri=input("Enter the string: ")
# import re
# count=0
# for i in stri:
#     z=ord(i)
#     if z>=97 and z<=122:
#         continue
#     elif z>=65 and z<=90:
#         continue
#     else:        count+=1
# print(count)

#Find the intersection of three arrays.Find common elements in three arrays.
# arr1=[1,2,3,4,5]
# arr2=[3,4,5,6,7]
# arr3=[5,6,4,8,9]
# def intersection(arr1,arr2,arr3):
#     for i in arr1:
#         if i in arr2 and i in arr3:
#             print(i)
#         else:
#             continue
# intersection(arr1,arr2,arr3)

# Move zeroes to the end without changing the order of the elements
# arr1=[1,0,122,3,4,0,5]
# def zeroestoend(arr1):
#     z=0
#     for z in arr1:
#         if z in arr1:
#             arr1.remove(z)
#             arr1.append(z)
#         else:
#             continue
#     print(arr1)

# arr2=[90,0,23,0,10,0,89,12]
# zeroestoend(arr2)

# Find the second largest element in an array
# arr1=[1,2,3,4,5]
# def secondlargest(arr1):
#     largest=arr1[0]
#     second_largest=arr1[0]
#     for i in arr1:
#         if i>largest:
#             second_largest=largest
#             largest=i
#         elif i>second_largest and i!=largest:
#             second_largest=i
#     return second_largest
# print(secondlargest(arr1))

# Write a program to calculate and return the sum of distances between the adjacent numbers in an array of positive numbers
def disbnums(index,arr):
    z=0
    for i in range(index-1):
        z+=abs(arr[i]-arr[i+1])
    return z
    
arr2=[1,2,3,4,5]
disbnums(3,arr2)




