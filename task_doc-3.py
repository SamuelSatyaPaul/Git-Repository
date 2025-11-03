# s=int(input("ent number:"))
# if s>0:
#     print("positive")
# elif s<0:
#     print("negative")
# elif s == 0:
#     print("zero")
# else:
#     print("not suitable")

# num1 = int(input("ent num1:"))
# num2 = int(input("ent num2:"))
# num3 = int(input("ent num3:"))
# if num1 > num2 and num3:
#     print("num1 is greater")
# elif num2 > num3 and num1:
#     print("num2 is greater")
# else:
#     print("num3 is greater")

# year = int(input("ent year:"))
# if year % 4== 0 and year % 100!=0:
#     print("leap year")
# else:
#     print("not leap year")

# side1 = int(input("ent num1:"))
# side2 = int(input("ent num2:"))
# side3 = int(input("ent num3:"))
# if side1+side2 > side3 and side2+side3 >side1 and side3+side1>side2:
#     print("triangle")
# else:
#     print("not a triangle")

# num=[]
# for i in range(1,26):
#     if i%2 ==0:
#         num+=[i] #adding to list also incresing
# print(num)

# num = int(input("ent num:"))
# for i in range(1,11):
#     print(num, "*", i, "=" ,num*i)

# n= 5
# prod=1
# for i in range(1,n+1):
#     prod *= i
# print(prod)

# n= 10
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(sum)

num = int(input("ent num:"))
while num>0:
    digit = num % 10
    print(digit)
    num = num // 10

# num = int(input("ent num:"))
# total = 0
# while num>0:
#     digit = num %10
#     total += digit
#     num = num //10
# print(total)