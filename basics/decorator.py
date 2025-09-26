# # decorator
# def clean_table(func):
#     def wrapper():
#         print("👉 Cup saaf kar rahe hain")
#         func()   # asal function chalega
#         print("👉 Table saaf kar rahe hain")
#     return wrapper

# # asal function
# @clean_table
# def make_tea():
#     print("🍵 Chai ban rahi hai")

# make_tea()
# built-in functionsc
def hello(func):
    def wrapper ():
        print("Hello Hamza Bhai")
        func()
        print("Hello Hamza Bhai Ye End Statement Hai")
    return wrapper

@hello 
def hello():
    print("Main Code hai ye wala")

hello()