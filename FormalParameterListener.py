from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from JavaListener import JavaListener

class FormalParameterListener(JavaListener):

	def __init__(self):
		self.arg = {}

	# Enter a parse tree produced by JavaParser#formalParameter.
	def enterFormalParameter(self, ctx:JavaParser.FormalParameterContext):

		self.arg["type"] = self.getAllText(ctx.typeType())
		#print("Arg Type : ",self.getAllText(ctx.typeType())) 

		if(ctx.variableDeclaratorId() != None):
			self.arg["name"] = self.getAllText(ctx.variableDeclaratorId())
			#print("Arg Name : ",self.getAllText(ctx.variableDeclaratorId()))

		if(ctx.variableModifier() != []):
			self.arg["modifier"] = self.getAllText(ctx.variableModifier())
			#print("Arg Modifier : ",ctx.variableModifier())

	# Exit a parse tree produced by JavaParser#formalParameter.
	def exitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
		pass

	# Enter a parse tree produced by JavaParser#lastFormalParameter.
	def enterLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		pass

	# Exit a parse tree produced by JavaParser#lastFormalParameter.
	def exitLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		pass