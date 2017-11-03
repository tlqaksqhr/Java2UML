from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from JavaListener import JavaListener
from ClassListener import ClassListener
from InterfaceListener import InterfaceListener

class CompilationUnitListener(JavaListener):

	def __init__(self):
		self.PackageName = ""
		self.Classes = []
		self.Interfaces = []

	# Enter a parse tree produced by JavaParser#compilationUnit.
	def enterCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):

		PackageName = self.getAllText(ctx.packageDeclaration().qualifiedName())
		print("Package Name : ",PackageName)

		Container = ctx.typeDeclaration()
		ClassContainer = []
		InterfaceContainer = []
		for typeDeclaration in Container:
			if(typeDeclaration.classDeclaration() != None):
				ClassContainer.append(typeDeclaration.classDeclaration())
			elif(typeDeclaration.interfaceDeclaration() != None):
				InterfaceContainer.append(typeDeclaration.interfaceDeclaration())

		for Class in ClassContainer:
			classListener = ClassListener()
			Class.enterRule(classListener)
			self.Classes.append(classListener.ClassNode)

		# TODO : Interface Parser implements...
		for Interface in InterfaceContainer:
			interfaceListener = InterfaceListener()
			Interface.enterRule(interfaceListener)
			self.Interfaces.append(interfaceListener.InterfaceNode)


	# Exit a parse tree produced by JavaParser#compilationUnit.
	def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
		pass