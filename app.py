# # bubble sort
# def bubble_sort(val):
#     n = len(val)
#     for j in range(n):
#         for i in range(1, n - j):
#             if val[i - 1] > val[i]:
#                 temp = val[i - 1]
#                 val[i - 1] = val[i]
#                 val[i] = temp
#     return val

# val = [32, 5, 3, 6, 7, 54, 87]
# print(bubble_sort(val))

# # Star triangle

# def star_tri(val):
#     count = val // 2

#     for i in range(1, val + 1, 2):
#         print(f"{" " * count}{"*" * i}")
#         count -= 1


# star_tri(9)

# # fiboniachi seriese:
# def fibo():
#     no_of_terms = int(input("Enter no of trems in there seriese: "))
#     before = 0
#     sum = 1
#     print (before,sum, end = " ")   
#     for _ in range(no_of_terms - 2):
#         temp = sum
#         sum = sum + before
#         print( sum, end = " ")
#         before = temp
# fibo()
 
# # Number is prime:
# inp_val = int(input("Enter a number: "))
# if inp_val < 2:
#     print ("False")
# else:
#     for i in range(2, (inp_val // 2) + 1 ):
#         if inp_val % i == 0:
#             print("False")
#             break
    
#     else:
#         print("True")

# # Palandrome
# arr =input("Enter sequence :")
# b = arr[::-1]
# if arr == b:
#     print("Palandrome")
# else:
#     print("Not a palandrome")    
        
# Upper letters:
def count_capitals(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    print(f"Number of capital letters: {count}")

text = input("Enter text: ") 
count_capitals(text)






