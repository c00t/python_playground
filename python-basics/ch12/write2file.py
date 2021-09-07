from pathlib import Path
hello_world_txt = Path.cwd() / Path("hello.txt")
print(f"Create file in {hello_world_txt}")
hello_world_txt.touch()
with hello_world_txt.open(mode="w", encoding="utf-8") as file:
    file.write("# hello.txt\n# encoding: UTF-8")

print("123".startswith("1"))