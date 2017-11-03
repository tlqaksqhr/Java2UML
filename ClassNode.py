from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser

class ClassNode():

	def __init__(self):
		self.ClassName = ""
		self.Extends = ""
		self.ImplementList = []
		self.MethodList = []
		self.FieldList = []

	def __str__(self):
		SerializedString = "{"
		SerializedString += "{}|".format(self.ClassName)
		for field in self.FieldList:
			SerializedString += "+ {} : {}\l".format(field["Identifier"],field["Type"])
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