from antlr4 import *
from .JavaLexer import JavaLexer
from .JavaParser import JavaParser
from .JavaListener import JavaListener
from .MethodListener import MethodListener
from .FieldListener import FieldListener
from .InterfaceListener import InterfaceListener
from .ClassNode import ClassNode

class ClassListener(JavaListener):

	def __init__(self):
		self.ClassNode = ClassNode

	# Enter a parse tree produced by JavaParser#classDeclaration.
	def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):

		Cnode = ClassNode()

		Cnode.ClassName = ctx.Identifier().getText()
		#print("Name : ", ctx.Identifier().getText())
		
		extends = ctx.typeType()
		if(type(extends) != type(None)):
			Cnode.Extends = self.getAllText(extends)
			#print("Extends : ", self.getAllText(extends))
		

		# TODO : interface name parsing
		implementList = ctx.typeList()

		if(type(implementList) != type(None)):
			implementList = implementList.typeType()
			for implement in implementList:
				#print("Implement : ", self.getAllText(implement))
				Cnode.ImplementList.append({"Type" : self.getAllText(implement)})

		classBodyDeclarations = ctx.classBody().classBodyDeclaration()
		MethodContainer = []
		FieldContainer = []

		for classBodyDeclaration in classBodyDeclarations:

			modifier = ""
			for mod in classBodyDeclaration.modifier():
				modifier = modifier + " " + self.getAllText(mod)
			if(type(classBodyDeclaration.memberDeclaration().methodDeclaration()) != type(None)):
				MethodContainer.append({"modifier" : modifier,"value" : classBodyDeclaration.memberDeclaration().methodDeclaration()})
			elif(type(classBodyDeclaration.memberDeclaration().constructorDeclaration()) != type(None)):
				MethodContainer.append({"modifier" : modifier,"value" : classBodyDeclaration.memberDeclaration().constructorDeclaration()})
			elif(type(classBodyDeclaration.memberDeclaration().fieldDeclaration()) != type(None)):
				FieldContainer.append({"modifier" : modifier,"value" : classBodyDeclaration.memberDeclaration().fieldDeclaration()})

		for Method in MethodContainer:
			methodListener = MethodListener()
			Method["value"].enterRule(methodListener)
			methodListener.Method["modifier"] = Method["modifier"]
			Cnode.MethodList.append(methodListener.Method)
			#print(methodListener.Method)

		for Field in FieldContainer:
			fieldListener = FieldListener()
			Field["value"].enterRule(fieldListener)
			for i in range(0,len(fieldListener.FieldList)):
				fieldListener.FieldList[i].update({"modifier" : Field["modifier"]})
			Cnode.FieldList += fieldListener.FieldList
			#print(methodListener.Method)			

		self.ClassNode = Cnode

		#print("Class Name : ", self.ClassNode.ClassName)
		#print("Class Extends : ", self.ClassNode.Extends)
		#print("Class Methods : ",self.ClassNode.MethodList)
		#print("Class Fields : ",self.ClassNode.FieldList)
		#print("Class Implements : ",self.ClassNode.ImplementList)
		#print(self.ClassNode)

	# Exit a parse tree produced by JavaParser#classDeclaration.
	def exitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		pass