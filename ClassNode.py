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
		SerializedString = "<{"
		SerializedString += "{}|".format(self.ClassName)
		for field in self.FieldList:
			if(field["modifier"].find("private") != -1):
				SerializedString += "~ "
			elif(field["modifier"].find("protected") != -1):
				SerializedString += "# "
			else:
				SerializedString += "+ "

			if field["modifier"].find("static") != -1:
				SerializedString += "<u>{} : {}</u><BR ALIGN=\"left\"/>".format(field["Identifier"],field["Type"])
			else:
				SerializedString += "{} : {}<BR ALIGN=\"left\"/>".format(field["Identifier"],field["Type"])
		
		SerializedString += "|"
		for method in self.MethodList:
			if(method["modifier"].find("private") != -1):
				SerializedString += "~ "
			elif(method["modifier"].find("protected") != -1):
				SerializedString += "# "
			else:
				SerializedString += "+ "

			if method["ReturnType"] == "@@@Constructor@@@":
				if field["modifier"].find("static") != -1:
					SerializedString += "<u>&lt;&lt;constructor&gt;&gt;{}{}</u><BR ALIGN=\"left\"/>".format(method["MethodName"],self.ArgumentSerialize(method))					
				else:
					SerializedString += "&lt;&lt;constructor&gt;&gt;{}{}<BR ALIGN=\"left\"/>".format(method["MethodName"],self.ArgumentSerialize(method))
			else:
				SerializedString += "{}{} : {}<BR ALIGN=\"left\"/>".format(method["MethodName"],self.ArgumentSerialize(method),method["ReturnType"])
		SerializedString += "}>"

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