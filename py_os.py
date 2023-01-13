import os

# Target directory

targetDir = "/demo/participant"
files = []
dirs  = []

for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
    dirs += dirnames
print(files)
print(dirs)
