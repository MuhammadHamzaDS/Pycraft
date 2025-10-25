spam_amount = 0
print (spam_amount)
spam_amount = spam_amount + 8
if spam_amount > 0:
    print("MY Name is Hamza,And I am a Python Developer")
    count = "Hamza" * spam_amount
    print(count)
    
    # These All are the Built-in Functions
print(type(spam_amount))
print(type(19.89))
hat_height = 25.4
hat_width = 10.8
# without parenthesis Answer is different
total_area = hat_height + hat_width /2 
print(total_area)
# with parenthesis
total_area = (hat_height + hat_width) /2
print(total_area)
print(min(1, 2, 3))
print(max(1, 2, 3))
print(abs(-9.8))
print(abs(9.8))
print(round(3.14159))
print(round(3.14159, 2))
print(pow(2, 3))
print(pow(5, 5))
# is me 4 modulos hai pow(2, 3, 4)   # (2^3) % 4
print(pow(2, 3, 4))
name = "Hamza"
print(len(name))   # 5
num = "25"
print(int(num) + 5)   # 30
numbers = [2, 8, 1, 6]
print(max(numbers))  # 8
print(min(numbers))  # 1
marks = [70, 80, 90]
print(sum(marks))   # 240
name = input("Apna naam likho: ")
print("Hello,", name)
print(round(3.7))   # 4
print(round(3.2))   # 3
nums = [4, 2, 9, 1]
print(sorted(nums))   # [1, 2, 4, 9]
for i in range(5):
    print(i)   # 0,1,2,3,4

print("My name is hamza what is your name")
for i in range(10):
    print(i) 