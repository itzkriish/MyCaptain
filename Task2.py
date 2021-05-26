file_name = input("Input the file name with extension (Python, Java or Text): ")
extensions = {".py": "Python", ".txt": "Text", ".java": "Java"}
file_type = extensions.get(file_name[file_name.index('.'):])
print("The extension of the file is:", file_type)
