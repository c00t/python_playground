from pathlib import Path
import shutil
cwd = Path.cwd()
new_folder = cwd / "my_folder"
new_folder.mkdir()
(new_folder / "file1.txt").touch()
(new_folder / "file2.txt").touch()
(new_folder / "image1.png").touch()
(new_folder / "images").mkdir()
(new_folder / "image1.png").replace(new_folder / "images" / "image1.png")

(new_folder / "file1.txt").unlink()

shutil.rmtree(new_folder)