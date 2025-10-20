# | Mode   | Use                                            |
# | ------ | ---------------------------------------------- |
# | `'r'`  | Read only (file must exist)                    |
# | `'w'`  | Write (creates new file or overwrite existing) |
# | `'a'`  | Append (add at the end of file)                |
# | `'r+'` | Read and Write                                 |


# File Ko Open krna
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
