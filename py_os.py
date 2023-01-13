import os

# Target directory
targetDir = r'd:\tmp\util\dist\check'
files = []
dirs  = []

# The three variables below, dirpath.dirnamesfilenames
# dirpath represents the directory name that is currently traversal
# dirnames is a list object that stores all the subclass names in the current dirpath
# filenames is a list object that stores all the file names in the current dirpath

for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
    dirs += dirnames

print(files)
print(dirs)
