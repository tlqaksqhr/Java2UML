import sys
from lib.Java2UML import Java2UML

def main(argv):
	MainClass = Java2UML()
	result = MainClass.JavaCode2UML(sys.argv[1])
	print(result)

if __name__ == '__main__':
	main(sys.argv)