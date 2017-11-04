from antlr4 import *
from .JavaLexer import JavaLexer
from .JavaParser import JavaParser
from .JavaListener import JavaListener

class FieldListener(JavaListener):

	def __init__(self):
		self.FieldList = []
		self.ConstList = []

	# Enter a parse tree produced by JavaParser#fieldDeclaration.
	def enterFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):

		vtype = ctx.typeType()
		if(type(vtype) == type(None)):
			vtype = "void"
		else:
			vtype = self.getAllText(vtype)


		variableDeclaratorList = ctx.variableDeclarators().variableDeclarator()

		#print("Field Type : ",vtype)
		for variableDeclarator in variableDeclaratorList:
			identifier = self.getAllText(variableDeclarator.variableDeclaratorId())
			self.FieldList.append({"Type" : vtype,"Identifier" : identifier})
			#print("Field identifier : ",identifier)
			

	# Exit a parse tree produced by JavaParser#fieldDeclaration.
	def exitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
		pass

	# Enter a parse tree produced by JavaParser#constDeclaration.
	def enterConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		ctype = ctx.typeType()
		if(type(ctype) == type(None)):
			ctype = "void"
		else:
			ctype = self.getAllText(ctype)

		constDeclaratorList = ctx.constantDeclarator()

		for constDeclarator in constDeclaratorList:
			identifier = self.getAllText(constDeclarator)
			self.ConstList.append({"Type" : ctype,"Identifier" : identifier})
			#print("Field identifier : ",identifier)

	# Exit a parse tree produced by JavaParser#constDeclaration.
	def exitConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		pass