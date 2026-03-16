#Function
# 1]
# def msg():  # called fuction
#     print("hello World")

# msg()

# 2]
# def add():
#     n1 = int(input("Enter The Value of n1 = "))
#     n2 = int(input("Enter The Value of n2 = "))
#     print("Add = ",n1+n2)
# add()

# 3] How To Written Multiple values
# def add():
#     n1 = int(input("Enter The Value of n1 = "))
#     n2 = int(input("Enter The Value of n2 = "))
#     sum = n1+n2 
#     mul = n1*n2 
#     div = n1/n2 
#     sub= n1-n2 
#     return sum,mul,div,sub
# result = add()
# print(result)

# 4]
# 1. Positional Argument
# 2. Keyword 
# 3. default
# 4. 

# 1. -> KeyWord Argument
# def personalInfo(fname, lname):
#     print("fristName = ",fname)
#     print("LastName = ",lname)

# fname = "Yash"
# lname = "Pokle"
# personalInfo(fname,lname)

# 2. -> default Argument
# def cityNmae(city = "Nagpur"):
#     print(city)

# cityNmae("Mumbai")
# cityNmae("Pune")
# cityNmae()

# variable Length argument
# def studentNames(*name): # This Variable(name) Take Number of Variables. In the Form Of "Tubles" 
#     print(name)

# studentNames("Yash","Sonu","Chiku","Jamal")
# myList = [5,2,9,7,5,6]
# # Search the Element
# def searchElement(target):
#     for i in range(len(myList)):  # myList = 6
#         # print(myList[i])
#         if target == myList[i]:
#             print("Element Found at index Number = ",i)
#     else:
#         print("Element Not Found")

# searchElement(11) # This Element We have to find

#2]
# myList = [5,2,9,7,5,6]
# # Search the Element
# def searchElement(target):
#     for i in range(len(myList)):  # myList = 6
#         # print(myList[i])
#         if target == myList[i]:
#             return i
#     print("Element Not Found")

# result = searchElement(3) # This Element We have to find
# print("Element Found at Index ",result)