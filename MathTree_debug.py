from MathTree import Node, BranchNode, LeafNode
import sys

tempNode = Node('+')
tempNode.addChild(Node(2))
tempNode.addChild(Node(3))
print(tempNode.children)

tempNode = Node('+',[Node(2),Node(3)])
print(tempNode.children)

tempNode = Node('+',(Node(2),Node(3)))
print(tempNode.children)
