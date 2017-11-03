from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from JavaListener import JavaListener
from FormalParameterListener import FormalParameterListener

class MethodListener(JavaListener):

	def __init__(self):
		self.ArgList = []
		self.Name = ""
		self.ReturnType = ""
		self.Method = {}

	# Enter a parse tree produced by JavaParser#methodDeclaration.
	def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		
		self.Name = ctx.Identifier().getText()
		#print("Method Name : ", ctx.Identifier().getText())
		
		rtype = ctx.typeType()
		if(type(rtype) == type(None)):
			rtype = "void"
		else:
			rtype = self.getAllText(rtype)

		self.ReturnType = rtype
		#print("Method Return Type : ", rtype) 
		
		formalParameters = ctx.formalParameters()

		if(type(formalParameters.formalParameterList()) == type(None)):
			parameters = { "type" : "void" }
			self.ArgList.append(parameters)
		else:
			formalParameterList = formalParameters.formalParameterList()
			for formalParameter in formalParameterList.formalParameter():
				if type(formalParameter) != type(None):
					formalParameterlistener = FormalParameterListener()
					formalParameter.enterRule(formalParameterlistener)
					self.ArgList.append(formalParameterlistener.arg)
					#print("Arg Type : ", self.getAllText(formalParameter))
			
			lastFormalParameter = formalParameterList.lastFormalParameter()
			if(lastFormalParameter != None):
				lastFormalParameter.enterRule(FormalParameterListener())
				#print("Arg Type : ", self.getAllText(formalParameterList.lastFormalParameter()))
		
		self.Method["MethodName"] = self.Name
		self.Method["ReturnType"] = self.ReturnType
		self.Method["ArgumentList"] = self.ArgList
	# Exit a parse tree produced by JavaParser#methodDeclaration.
	def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		pass

	# Enter a parse tree produced by JavaParser#interfaceMethodDeclaration.
	def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		self.Name = ctx.Identifier().getText()
		#print("Method Name : ", ctx.Identifier().getText())
		
		rtype = ctx.typeType()
		if(type(rtype) == type(None)):
			rtype = "void"
		else:
			rtype = self.getAllText(rtype)

		self.ReturnType = rtype
		#print("Method Return Type : ", rtype) 
		
		formalParameters = ctx.formalParameters()

		if(type(formalParameters.formalParameterList()) == type(None)):
			parameters = { "type" : "void" }
			self.ArgList.append(parameters)
		else:
			formalParameterList = formalParameters.formalParameterList()
			for formalParameter in formalParameterList.formalParameter():
				if type(formalParameter) != type(None):
					formalParameterlistener = FormalParameterListener()
					formalParameter.enterRule(formalParameterlistener)
					self.ArgList.append(formalParameterlistener.arg)
					#print("Arg Type : ", self.getAllText(formalParameter))
			
			lastFormalParameter = formalParameterList.lastFormalParameter()
			if(lastFormalParameter != None):
				lastFormalParameter.enterRule(FormalParameterListener())
				#print("Arg Type : ", self.getAllText(formalParameterList.lastFormalParameter()))
		
		self.Method["MethodName"] = self.Name
		self.Method["ReturnType"] = self.ReturnType
		self.Method["ArgumentList"] = self.ArgList
		pass

	# Exit a parse tree produced by JavaParser#interfaceMethodDeclaration.
	def exitInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		pass

	# Enter a parse tree produced by JavaParser#constructorDeclaration.
	def enterConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		
		self.Name = ctx.Identifier().getText()
		self.ReturnType = "@@@Constructor@@@"
		
		formalParameters = ctx.formalParameters()

		if(type(formalParameters.formalParameterList()) == type(None)):
			parameters = { "type" : "void" }
			self.ArgList.append(parameters)
		else:
			formalParameterList = formalParameters.formalParameterList()
			for formalParameter in formalParameterList.formalParameter():
				if type(formalParameter) != type(None):
					formalParameterlistener = FormalParameterListener()
					formalParameter.enterRule(formalParameterlistener)
					self.ArgList.append(formalParameterlistener.arg)
					#print("Arg Type : ", self.getAllText(formalParameter))
			
			lastFormalParameter = formalParameterList.lastFormalParameter()
			if(lastFormalParameter != None):
				lastFormalParameter.enterRule(FormalParameterListener())
				#print("Arg Type : ", self.getAllText(formalParameterList.lastFormalParameter()))

		self.Method["MethodName"] = self.Name
		self.Method["ReturnType"] = self.ReturnType
		self.Method["ArgumentList"] = self.ArgList

	# Exit a parse tree produced by JavaParser#constructorDeclaration.
	def exitConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		pass