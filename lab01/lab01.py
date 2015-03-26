import os
from os.path import getsize
import operator

def getDirectorySize(pathname = '.'):
	"""
	Function responsible for calculating size of given directory. 
	Apart from size of the directory, it returns name and size of largest file in that directory.
	It searches through all sub-directories recursively.

	Args:
		pathname(str, optional): directory pathname. Defaults to current directory.
	
	Eeturns:
		tuple contatining size of the directory, name of the largest file and size of the largest file
	
	"""
	size = {'root' : 0}
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(pathname):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
			size[fp] = os.path.getsize(fp)
	return total_size, max(size, key=size.get), size[max(size, key=size.get)]


print("enter pathname:", end="\t")
dirName = input()

total, largestName, largestSize = getDirectorySize(dirName)

print("size of directory", dirName, ":", total, "bytes")
print("largest filename:", largestName, ", largest file size: ", largestSize, "bytes")
