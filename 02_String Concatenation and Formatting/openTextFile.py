from pathlib import Path

file_path = Path("E:/Courses/youtube")
file_name = file_path / "test.txt"

f = open(file_name)
print (f.read())