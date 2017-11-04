import sys
from antlr4 import *
from .JavaLexer import JavaLexer
from .JavaParser import JavaParser
from .JavaListener import JavaListener
from .CompilationUnitListener import CompilationUnitListener
from .UMLGraph import UMLGraph

class Java2UML():


	def InitalizeSymbolTable(symbolTable,Classes,Interfaces):

		for Class in Classes:
			symbolTable[Class.ClassName] = 1

		for Interface in Interfaces:
			if Interface.InterfaceName in symbolTable:
				return -1
			else:
				symbolTable[Interface.InterfaceName] = 1

		return 1


	def JavaCode2UML(self,string):	
		#input = FileStream(string)
		#lexer = JavaLexer(input)

		lexer = JavaLexer(InputStream(string))
		stream = CommonTokenStream(lexer)
		parser = JavaParser(stream)
		tree = parser.compilationUnit()
		walker = ParseTreeWalker()
		listener = CompilationUnitListener()
		walker.walk(listener, tree)

		Classes = listener.Classes
		Interfaces = listener.Interfaces
		symbolTable = {}

		error = InitalizeSymbolTable(symbolTable,Classes,Interfaces)

		if(error < 0):
			return False

		graph = UMLGraph()
		
		for Interface in Interfaces:
			graph.addInterface(Interface)

		for Class in Classes:
			graph.addClass(Class)
			if Class.Extends in symbolTable:
				graph.addExtendsRelation(Class.ClassName,Class.Extends)
			for interface in Class.ImplementList:
				if interface["Type"] in symbolTable:
					graph.addImplementsRelation(Class.ClassName,interface["Type"])

		return str(graph)


def InitalizeSymbolTable(symbolTable,Classes,Interfaces):

		for Class in Classes:
			symbolTable[Class.ClassName] = 1

		for Interface in Interfaces:
			if Interface.InterfaceName in symbolTable:
				return -1
			else:
				symbolTable[Interface.InterfaceName] = 1

		return 1

def main(argv):
	input = FileStream(argv[1])
	lexer = JavaLexer(input)
	stream = CommonTokenStream(lexer)
	parser = JavaParser(stream)
	tree = parser.compilationUnit()
	walker = ParseTreeWalker()
	listener = CompilationUnitListener()
	walker.walk(listener, tree)

	Classes = listener.Classes
	Interfaces = listener.Interfaces
	symbolTable = {}

	error = InitalizeSymbolTable(symbolTable,Classes,Interfaces)

	if(error < 0):
		return False

	graph = UMLGraph()
	
	for Interface in Interfaces:
		graph.addInterface(Interface)

	for Class in Classes:
		graph.addClass(Class)
		if Class.Extends in symbolTable:
			graph.addExtendsRelation(Class.ClassName,Class.Extends)
		for interface in Class.ImplementList:
			if interface["Type"] in symbolTable:
				graph.addImplementsRelation(Class.ClassName,interface["Type"])


	print(str(graph))
 
#if __name__ == '__main__':
	#main(sys.argv)
	#MainClass = Java2UML()
	#result = MainClass.JavaCode2UML(sys.argv[1])
	#print(result)