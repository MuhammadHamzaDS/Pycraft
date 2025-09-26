# decorator
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
