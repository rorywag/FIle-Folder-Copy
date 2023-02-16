import shutil
from pathlib import Path

print("Ensure that the terminal you are using has Adminsitrator privileges otherwise copying may not be successful in some instances.")

#User input of the source and destination for the files to copied from and to.
s = Path(input("Enter the source directory you would like to copy: \n"))
d = Path(input("Enter the location you would like the directory to be dumped to: \n"))

def dirCopy(s, d):
    """"Try to copy source folder or file to destination.
    If this fails the func will out put the error."""
    try:
        shutil.copytree(s, d)
        print(f"Directory {s} successfully copied to {d}")
    except Exception as e:
        print(f"Failed to copy directory {s} to {d}: {e}")

dirCopy(s, d)