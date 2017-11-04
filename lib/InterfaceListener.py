from antlr4 import *
from .JavaLexer import JavaLexer
from .JavaParser import JavaParser
from .JavaListener import JavaListener
from .MethodListener import MethodListener
from .FieldListener import FieldListener
from .InterfaceNode import InterfaceNode

class InterfaceListener(JavaListener):

	def __init__(self):
		self.InterfaceNode = ""

	# Enter a parse tree produced by JavaParser#interfaceDeclaration.
	def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):

		INode = InterfaceNode()
		INode.InterfaceName = ctx.Identifier().getText()

		extendsList = ctx.typeList()

		if(type(extendsList) != type(None)):
			extendsList = extendsList.typeType()
			for extend in extendsList:
				INode.ExtendsList.append({"type" : self.getAllText(extend)})
				print("extends(Interface) : ", self.getAllText(extend))

		interfaceBodyDeclarations = ctx.interfaceBody().interfaceBodyDeclaration()
		MethodContainer = []
		ConstContainer = []

		for interfaceBodyDeclaration in interfaceBodyDeclarations:
			if(type(interfaceBodyDeclaration.interfaceMemberDeclaration().interfaceMethodDeclaration()) != type(None)):
				MethodContainer.append(interfaceBodyDeclaration.interfaceMemberDeclaration().interfaceMethodDeclaration())
			elif(type(interfaceBodyDeclaration.interfaceMemberDeclaration().constDeclaration()) != type(None)):
				ConstContainer.append(interfaceBodyDeclaration.interfaceMemberDeclaration().constDeclaration())

		for Method in MethodContainer:
			methodListener = MethodListener()
			Method.enterRule(methodListener)
			INode.MethodList.append(methodListener.Method)
			#print(methodListener.Method)

		for Const in ConstContainer:
			fieldListener = FieldListener()
			Const.enterRule(fieldListener)
			INode.ConstList += fieldListener.ConstList
			#print(methodListener.Method)

		print(INode.InterfaceName)
		self.InterfaceNode = INode

		print("Interface Name : ", self.InterfaceNode.InterfaceName)
		print("Interface ExtendsList : ", self.InterfaceNode.ExtendsList)
		print("Interface MethodList : ", self.InterfaceNode.MethodList)
		print("Interface ConstList : ", self.InterfaceNode.ConstList)

	# Exit a parse tree produced by JavaParser#interfaceDeclaration.
	def exitInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
		pass