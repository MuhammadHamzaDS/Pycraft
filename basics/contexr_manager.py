# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)
# # Write
with open("data.txt", "w") as f:
    f.write("Hello Hamza!\n")
    f.write("This is written using context manager.\n")

# Read
with open("data.txt", "r") as f:
    data = f.read()
    print(data)

with open("data.txt", "w") as f:
    f.write("My Name is Muhammad Hamza\n")
    f.write("SP23-BCS-093")

# Agar overwrite nahi karna (sirf add karna ho)
# with open("data.txt","r") as f:
#     data = f.read()
#     print (data)with open("data.txt", "a") as f:
#     f.write("Ye line end me add hogi.\n")
