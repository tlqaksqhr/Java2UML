from graphviz import Digraph
from ClassNode import ClassNode
from InterfaceNode import InterfaceNode

class UMLGraph():

	def __init__(self):
		self.Graph = Digraph('UMLGraph')
		self.Graph.attr('node', fontname = "Bitstream Vera Sans", shape = "record" \
			, fontsize = "9", height = "1", width = "4")
		self.Graph.attr('edge', fontname = "Bitstream Vera Sans", fontsize = "9")

	def __str__(self):
		return self.Graph.source

	def addClass(self,Classnode):
		self.Graph.node(Classnode.ClassName,label=str(Classnode))

	def addInterface(self,Interfacenode):
		self.Graph.node(Interfacenode.InterfaceName,label=str(Interfacenode))

	# TODO : Direction option add is needed
	def addExtendsRelation(self,ClassName,ExtendsName):
		self.Graph.edge(ExtendsName,ClassName,arrowtail = "empty",dir="back")

	def addImplementsRelation(self,ClassName,interfaceName):
		self.Graph.edge(interfaceName,ClassName,arrowtail = "empty",style="dashed", dir="back")