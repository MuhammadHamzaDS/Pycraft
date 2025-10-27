# decorator:Function ki functionality ko modify karne ka ek tareeqa hai bina us function ke code ko badle
# decorator ek function ko leta hai aur ek naya function return karta hai jo asal function ki functionality ko enhance ya modify karta hai
def clean_table(func):
    def wrapper():
        print("👉 Cup saaf kar rahe hain")
        func()   # asal function chalega
        print("👉 Table saaf kar rahe hain")
    return wrapper

# asal function
@clean_table
def make_tea():
    print("🍵 Chai ban rahi hai")

make_tea()
# built-in functionsc
def hello(func):
    def wrapper ():
        print("Hello Hamza Bhai")
        func()
        print("YE function k baad wali hai")
    return wrapper

@hello 
def hello():
    print("Main Code hai ye wala")

hello()