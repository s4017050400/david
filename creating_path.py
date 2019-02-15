import os

filename = "/foo/bar/baz.txt"¨ #first '/' means a 'C:' if no 'no' means 'wtcwd'
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("FOOBAR")
