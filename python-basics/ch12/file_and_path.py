import pathlib

some_path = pathlib.Path(r"C:/Users/sh33p/")
print(some_path)

home = pathlib.Path.home()
hello_txt = home / "Desktop" / "Hello.txt"
print(hello_txt)

rel_path = pathlib.Path("/Users/sh33p/")
print(rel_path.is_absolute())

print(rel_path.resolve())