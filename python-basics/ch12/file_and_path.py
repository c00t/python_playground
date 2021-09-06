import pathlib

some_path = pathlib.Path(r"C:/Users/sh33p/")
print(some_path)

home = pathlib.Path.home()
hello_txt = home / "Desktop" / "Hello.txt"
print(hello_txt)

rel_path = pathlib.Path("/Users/sh33p/")
print(rel_path.is_absolute())

print(rel_path.resolve())

print(type(some_path.parents))
# <class 'pathlib._PathParents'>

# check what is `.is_dir()` return if directory not exist, or is a file?
not_exist_path = pathlib.Path("C:/Users/123")
a_file_path = pathlib.Path("C:/Users/sh33p/.ssh/id_rsa.pub")

print(not_exist_path.is_dir())
print(a_file_path.is_dir())

print("--Below are exercises--")
file_path = pathlib.Path.home() / "my_folder/my_file.txt"
print(file_path)
print(f"Existed or not?{file_path.exists()}")
print("Name is:" + file_path.name)
print("Parent folder name:" + file_path.parent.name)

print("--Create a file in cwd()/zzz.txt")
new_file_path = pathlib.Path.cwd() / "zzz.txt"
# new_file_path.touch(exist_ok=True)

for path in some_path.iterdir():
    print(path)

print("-----")
for path in new_file_path.parent.glob("*.txt"):
    print(path)
# for path in new_file_path.parent.glob("z?+.txt"):
#     print(path)

for path in new_file_path.parent.parent.rglob("*.py"):
    print(path)

replace_filename = new_file_path.parent / "xxx.txt"
# new_file_path.replace(replace_filename)

# 文件夹不存在的时候，同样会报出Error
# not_exist_folder = pathlib.Path.cwd() / "folder_a" / "xxx.txt"
# replace_filename.replace(not_exist_folder)