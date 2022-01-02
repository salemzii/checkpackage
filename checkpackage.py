import sys
import os

name = sys.argv[1]


def checkpage(name : str) -> bool:
	os.system("pip freeze > pylist.txt")

	with open("pylist.txt", "r") as rdlist:
		file = rdlist.readlines()
		for line in file:
			print(line)
			if str(line).startswith(name):
				return True
			continue
		return False


print(checkpage(name))
