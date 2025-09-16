help(round)
mystery = print()
print(mystery)

num = int(input("Enter a number: "))

# Table print karna
print(f"\nTable of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
