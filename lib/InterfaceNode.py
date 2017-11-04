from antlr4 import *
from .JavaLexer import JavaLexer
from .JavaParser import JavaParser

class InterfaceNode():

	def __init__(self):
		self.InterfaceName = ""
		self.ExtendsList = []
		self.MethodList = []
		self.ConstList = []


	def __str__(self):
		SerializedString = "{"
		SerializedString += "\<\<interface\>\>\\n{}|".format(self.InterfaceName)
		for const in self.ConstList:
			identifier,intializer = const["Identifier"].split("=")
			SerializedString += "+ {}: {} = {}\l".format(identifier,const["Type"],intializer)
		SerializedString += "|"
		for method in self.MethodList:
			SerializedString += "+ {}{} : {}\l".format(method["MethodName"],self.ArgumentSerialize(method),method["ReturnType"])
		SerializedString += "}"

		return SerializedString

	def ArgumentSerialize(self,method):
		SerializedString = "("

		length = len(method["ArgumentList"])
		i = 1

		for argument in method["ArgumentList"]:
			SerializedString += argument["type"]
			if argument["type"] != "void":
				SerializedString += (" : " + argument["name"])
				if i != length:
					SerializedString += ", "
			i += 1
		SerializedString += ")"
		return SerializedString