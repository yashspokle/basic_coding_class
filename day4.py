# # 1. zip() with continue
# print("1. zip() with continue")
# for i, j in zip(range(1, 6), range(5, 0, -1)):
#     if i == 3 and j == 3:
#         continue
#     print(i, j)

# print("\n2. while loop from 1 to 5")
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print("\n3. Username and password check")
# username = ""
# password = ""

# while username != "admin" or password != "hello":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# print("Login successful")

# print("\n4. Sum of first n natural numbers")
# n = int(input("Enter a number: "))
# total = 0
# i = 1

# while i <= n:
#     total += i
#     i += 1

# print(f"The sum of first {n} numbers is: {total}")

# print("\n5. Remove duplicate characters")
# name = "prashant"
# new_name = ""

# for ch in name:
#     if ch not in new_name:
#         new_name += ch

# print("Original string :", name)
# print("Without duplicates:", new_name)

# print("\n6. Reverse a string")
# name = "prashant"
# print("Original string :", name)
# print("Reversed string :", name[::-1])

# print("\n7. Cart items")
# my_cart = [10, 20, 200, 300, 800, 60, 700]

# for item in my_cart:
#     if item > 400:
#         print(f"{item} -> Expensive item")
#     else:
#         print(f"{item} -> Normal item")

# print("\n8. Palindrome check")
# text = input("Enter a string: ").lower()

# if text == text[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

# print("\n9. Number pattern")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, end=" ")
#     print()

print("\n10. Alphabet square pattern")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()  